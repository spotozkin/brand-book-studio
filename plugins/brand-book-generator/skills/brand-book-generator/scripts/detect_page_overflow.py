#!/usr/bin/env python3
"""
Page-overflow detector — finds content that escaped its margin, automatically.

Why this exists: flexbox layouts in WeasyPrint can silently overflow a page's
declared margin (a column refusing to shrink below its longest word, a pill
refusing to wrap, a badge growing past its box) while the render still
completes with no error and the right page count. That failure is invisible
to any code-level check and easy to miss in a quick visual skim — it was
caught twice in the same book (a button, then a footer) only because a person
looked closely at exactly the right page. This script replaces "hope you
looked at the right page" with a mechanical, page-agnostic check: every page
should be blank within its own declared margin, and if it isn't, something
broke its box.

Usage:
    python3 detect_page_overflow.py brand_book.pdf brand_book.html
    python3 detect_page_overflow.py brand_book.pdf brand_book.html --skip-pages 1,30
    python3 detect_page_overflow.py brand_book.pdf brand_book.html --dpi 150 --threshold 40

Requires: pdf2image, Pillow, numpy (all already used elsewhere in this skill's workflow).

What it does:
  1. Parses the `.page { padding: ... }` rule out of the HTML to learn the
     page's own declared margins (falls back to sensible CSS defaults, or
     pass --margins explicitly as "top,right,bottom,left" in inches).
  2. Rasterizes every PDF page at the given DPI.
  3. For each page, samples the four margin bands (top/right/bottom/left) and
     counts non-background pixels in each.
  4. Flags any band whose count exceeds --threshold as a probable overflow.

What it deliberately does NOT do:
  - It does not understand full-bleed pages (covers, color dividers). Pass
    their page numbers to --skip-pages, or expect (and manually confirm) that
    they'll be flagged as "overflow" on all four sides — that is correct
    behavior for an intentional full-bleed page, not a bug.
  - The bottom band routinely contains the page's own folio (page number /
    running header) by design in this skill's templates — a small, expected
    hit there is normal. This script still reports it (so you can eyeball the
    count once) but a bottom-only hit in the range of ordinary folio text
    (a few hundred px at 150dpi) is not the same signal as a left/right hit,
    which has no legitimate reason to exist on a non-bleed page and should be
    treated as a near-certain bug.

This is a detector, not a fixer. A flagged page still needs a human/model
look to confirm and to pick the right structural fix (add flex-shrink:0,
add min-width:0, add flex-wrap:wrap — see references/rendering_pitfalls.md).
"""
import argparse
import re
import sys


def parse_page_margins_inches(html_path):
    """Extract the .page{padding:...} rule from the book's HTML.
    Returns (top, right, bottom, left) in inches, or None if not found."""
    try:
        html = open(html_path, encoding="utf-8").read()
    except OSError:
        return None
    m = re.search(r"\.page\s*\{[^}]*padding:\s*([^;]+);", html)
    if not m:
        return None
    parts = m.group(1).strip().split()
    vals = []
    for p in parts:
        pm = re.match(r"([\d.]+)(in|pt|px)?", p)
        if not pm:
            return None
        num = float(pm.group(1))
        unit = pm.group(2) or "in"
        if unit == "pt":
            num = num / 72.0
        elif unit == "px":
            num = num / 96.0
        vals.append(num)
    if len(vals) == 1:
        return (vals[0],) * 4
    if len(vals) == 2:
        return (vals[0], vals[1], vals[0], vals[1])
    if len(vals) == 3:
        return (vals[0], vals[1], vals[2], vals[1])
    if len(vals) == 4:
        return tuple(vals)
    return None


def check_pdf(pdf_path, html_path=None, dpi=150, threshold=40, bottom_threshold=None,
              skip_pages=None, margins_in=None, bg_tolerance=5):
    from pdf2image import convert_from_path
    from PIL import Image
    import numpy as np

    skip_pages = set(skip_pages or [])
    if bottom_threshold is None:
        # the folio (page number / running header) legitimately lives in the
        # bottom margin in this skill's templates — give it real headroom so
        # it doesn't drown out genuine left/right/top overflow signals.
        bottom_threshold = threshold * 40

    margins = margins_in
    if margins is None and html_path:
        margins = parse_page_margins_inches(html_path)
    if margins is None:
        margins = (0.75, 0.75, 0.75, 0.75)  # conservative fallback

    top_in, right_in, bottom_in, left_in = margins
    print(f"Using margins (in): top={top_in} right={right_in} "
          f"bottom={bottom_in} left={left_in}  @ {dpi} dpi")
    print(f"Thresholds (px): top/left/right={threshold}  bottom={bottom_threshold} "
          f"(bottom is higher because the folio lives there by design)")

    pages = convert_from_path(pdf_path, dpi=dpi)
    flagged = []

    for i, page in enumerate(pages, start=1):
        if i in skip_pages:
            continue
        arr = np.array(page.convert("RGB"))
        H, W, _ = arr.shape
        top_px = int(top_in * dpi)
        right_px = int(right_in * dpi)
        bottom_px = int(bottom_in * dpi)
        left_px = int(left_in * dpi)

        def nonbg_count(band):
            if band.size == 0:
                return 0
            light = (band[:, :, 0] > 255 - bg_tolerance) & \
                    (band[:, :, 1] > 255 - bg_tolerance) & \
                    (band[:, :, 2] > 255 - bg_tolerance)
            nonlight = ~light
            if not nonlight.any():
                return 0
            # Ignore pixels only in the outermost 2px of the band — that's
            # normal font/rule anti-aliasing grazing the boundary line, not
            # real overflow. Real overflow content is inset further than that.
            core = nonlight[:, 2:-2] if nonlight.shape[1] > 4 else nonlight
            return int(core.sum())

        counts = {
            "top": nonbg_count(arr[:top_px, :]),
            "right": nonbg_count(arr[:, W - right_px:]),
            "bottom": nonbg_count(arr[H - bottom_px:, :]),
            "left": nonbg_count(arr[:, :left_px]),
        }

        side_thresholds = {"top": threshold, "right": threshold,
                            "left": threshold, "bottom": bottom_threshold}
        hit_sides = {k: v for k, v in counts.items() if v > side_thresholds[k]}
        if hit_sides:
            flagged.append((i, hit_sides))

    print()
    if not flagged:
        print(f"Clean: no margin overflow above threshold={threshold} "
              f"on any checked page.")
        return 0

    print(f"Flagged {len(flagged)} page(s):")
    for pageno, sides in flagged:
        parts = ", ".join(f"{k}={v}px" for k, v in sides.items())
        severity = "LIKELY BUG" if ("left" in sides or "right" in sides or "top" in sides) else "check folio"
        print(f"  page {pageno}: {parts}   [{severity}]")
    print()
    print("left/right/top hits on a non-bleed page are near-certain overflow —")
    print("see references/rendering_pitfalls.md for the fix pattern (flex-shrink:0,")
    print("min-width:0, flex-wrap:wrap). bottom-only hits are usually the folio;")
    print("confirm the pixel count looks like page-number text, not a UI block.")
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", help="Rendered PDF to check")
    ap.add_argument("html", nargs="?", default=None,
                     help="Source HTML (used to auto-detect .page margins)")
    ap.add_argument("--dpi", type=int, default=150)
    ap.add_argument("--threshold", type=int, default=40,
                     help="Non-background pixel count above which a margin band is flagged")
    ap.add_argument("--bottom-threshold", type=int, default=None,
                     help="Separate (higher) threshold for the bottom band, which "
                          "legitimately contains the folio. Defaults to 40x --threshold.")
    ap.add_argument("--skip-pages", default="",
                     help="Comma-separated 1-indexed page numbers to skip (full-bleed covers, dividers)")
    ap.add_argument("--margins", default=None,
                     help="Override margins as 'top,right,bottom,left' in inches, "
                          "skipping HTML auto-detection")
    args = ap.parse_args()

    skip = [int(x) for x in args.skip_pages.split(",") if x.strip()]
    margins = None
    if args.margins:
        margins = tuple(float(x) for x in args.margins.split(","))

    sys.exit(check_pdf(args.pdf, args.html, dpi=args.dpi, threshold=args.threshold,
                        bottom_threshold=args.bottom_threshold,
                        skip_pages=skip, margins_in=margins))


if __name__ == "__main__":
    main()
