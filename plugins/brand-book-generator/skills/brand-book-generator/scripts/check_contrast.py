#!/usr/bin/env python3
"""
WCAG contrast ratio checker for brand color pairs.

Usage:
    python3 check_contrast.py "#1A2B3C" "#FFFFFF"
    python3 check_contrast.py "#1A2B3C" "#FFFFFF" --large

Or import and call check_pair() / check_palette() directly for multiple pairs.
"""

import sys
import argparse


def _hex_to_rgb(hex_color):
    h = hex_color.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"Invalid hex color: {hex_color}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _relative_luminance(rgb):
    def channel(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(hex_a, hex_b):
    lum_a = _relative_luminance(_hex_to_rgb(hex_a))
    lum_b = _relative_luminance(_hex_to_rgb(hex_b))
    lighter, darker = max(lum_a, lum_b), min(lum_a, lum_b)
    return (lighter + 0.05) / (darker + 0.05)


def check_pair(hex_a, hex_b, large_text=False, label=""):
    ratio = contrast_ratio(hex_a, hex_b)
    normal_min, large_min, ui_min = 4.5, 3.0, 3.0
    threshold = large_min if large_text else normal_min
    passes_text = ratio >= threshold
    passes_ui = ratio >= ui_min
    prefix = f"[{label}] " if label else ""
    print(f"{prefix}{hex_a} on {hex_b}: ratio = {ratio:.2f}:1")
    kind = "large text" if large_text else "normal text"
    print(f"  {kind} (needs {threshold}:1): {'PASS' if passes_text else 'FAIL'}")
    print(f"  non-text UI/graphics (needs {ui_min}:1): {'PASS' if passes_ui else 'FAIL'}")
    return {"ratio": ratio, "passes_text": passes_text, "passes_ui": passes_ui}


def check_palette(pairs):
    """pairs: list of (hex_a, hex_b, label, large_text) tuples"""
    results = []
    for hex_a, hex_b, label, large_text in pairs:
        results.append(check_pair(hex_a, hex_b, large_text=large_text, label=label))
        print()
    failed = [r for r in results if not r["passes_text"]]
    if failed:
        print(f"⚠ {len(failed)} pairing(s) fail text contrast — pick a different pairing or a darker/lighter variant.")
    else:
        print("✓ All checked pairings pass.")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check WCAG contrast ratio between two hex colors.")
    parser.add_argument("color_a", help="First hex color, e.g. #1A2B3C")
    parser.add_argument("color_b", help="Second hex color, e.g. #FFFFFF")
    parser.add_argument("--large", action="store_true", help="Check against large-text threshold (3:1) instead of normal text (4.5:1)")
    args = parser.parse_args()
    check_pair(args.color_a, args.color_b, large_text=args.large)
