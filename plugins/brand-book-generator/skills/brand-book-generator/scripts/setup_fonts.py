#!/usr/bin/env python3
"""
Fetch real, renderable font files for the brand book PDF.

This environment can't reach fonts.googleapis.com directly, but npm's
registry IS reachable, and the @fontsource/* packages bundle the actual
Google Fonts .woff2 files inside the npm package. This script installs
the requested font packages and copies the specific weight/style files
you need into a local ./fonts/ folder, then prints the @font-face CSS
block to paste into the template's <style> section.

Usage:
    python3 setup_fonts.py <display-font-slug> <body-font-slug> [output_dir]

Example:
    python3 setup_fonts.py archivo-black space-grotesk .
    # installs @fontsource/archivo-black and @fontsource/space-grotesk,
    # copies 400 and 700 weight files into ./fonts/, prints @font-face CSS

Find slugs at https://fontsource.org or in references/font_pairings.md —
the slug is the part after "@fontsource/" (e.g. "archivo-black", "fraunces").
"""

import json
import os
import shutil
import subprocess
import sys


def npm_install(slugs, workdir):
    subprocess.run(
        ["npm", "install"] + [f"@fontsource/{s}" for s in slugs] + ["--silent", "--no-save"],
        cwd=workdir, check=True
    )


def get_family_name(slug, workdir):
    meta_json = os.path.join(workdir, "node_modules", "@fontsource", slug, "metadata.json")
    with open(meta_json) as f:
        data = json.load(f)
    return data.get("family", slug)


def copy_weights(slug, workdir, out_dir, weights=("400", "700")):
    files_dir = os.path.join(workdir, "node_modules", "@fontsource", slug, "files")
    copied = []
    for weight in weights:
        # prefer plain "latin" subset over "latin-ext" / "vietnamese" etc.
        candidates = [
            f for f in os.listdir(files_dir)
            if f.startswith(f"{slug}-latin-{weight}-normal") and f.endswith(".woff2")
        ]
        if not candidates:
            candidates = [
                f for f in os.listdir(files_dir)
                if f"-{weight}-normal" in f and f.endswith(".woff2")
            ]
        if not candidates:
            print(f"  (no {weight} weight found for {slug}, skipping)")
            continue
        src = os.path.join(files_dir, candidates[0])
        dst_name = f"{slug}-{weight}.woff2"
        dst = os.path.join(out_dir, dst_name)
        shutil.copyfile(src, dst)
        copied.append((weight, dst_name))
    return copied


def font_face_css(family, slug, copied):
    rules = []
    for weight, filename in copied:
        rules.append(
            f"@font-face {{\n"
            f"  font-family: '{family}';\n"
            f"  src: url('fonts/{filename}') format('woff2');\n"
            f"  font-weight: {weight};\n"
            f"  font-style: normal;\n"
            f"}}"
        )
    return "\n".join(rules)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    display_slug, body_slug = sys.argv[1], sys.argv[2]
    out_root = sys.argv[3] if len(sys.argv) > 3 else "."
    fonts_dir = os.path.join(out_root, "fonts")
    os.makedirs(fonts_dir, exist_ok=True)

    workdir = "/tmp/_font_fetch"
    if os.path.exists(workdir):
        shutil.rmtree(workdir)
    os.makedirs(workdir, exist_ok=True)

    print(f"Installing @fontsource/{display_slug} and @fontsource/{body_slug} ...")
    npm_install([display_slug, body_slug], workdir)

    css_blocks = []
    for slug, weights in [(display_slug, ("400", "700")), (body_slug, ("400", "700"))]:
        family = get_family_name(slug, workdir)
        copied = copy_weights(slug, workdir, fonts_dir, weights)
        css_blocks.append(font_face_css(family, slug, copied))
        print(f"  {family}: copied {[w for w, _ in copied]}")

    print("\n--- Paste this into the template's <style>, before :root ---\n")
    print("\n\n".join(css_blocks))
    print(f"\n--- Fonts copied to {fonts_dir}/ — keep this folder next to your HTML file ---")


if __name__ == "__main__":
    main()
