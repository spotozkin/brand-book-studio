#!/usr/bin/env python3
"""Committed choice — deterministic selection for genuinely free structural choices.

Usage:
    python3 committed_choice.py "<brand>" "<YYYY-MM-DD>" "<choice-label>" "optA|optB|optC"

Derives the pick from sha256(brand|date|label) so the model cannot re-roll toward its
comfort default. Use ONLY for choices that remain free after the central question,
seeds, and author profile have all spoken — never as a substitute for derivation.
Log the result in the SEEDS comment as: label=<option> (committed).
"""
import hashlib
import sys


def committed_choice(brand: str, date: str, label: str, options: list[str]) -> str:
    if len(options) < 2:
        raise ValueError("A committed choice needs at least two options.")
    key = f"{brand.strip().lower()}|{date.strip()}|{label.strip().lower()}"
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
    return options[int(digest, 16) % len(options)]


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(__doc__)
        sys.exit(1)
    brand, date, label, raw = sys.argv[1:5]
    options = [o.strip() for o in raw.split("|") if o.strip()]
    pick = committed_choice(brand, date, label, options)
    print(f"{label} = {pick}  (committed from {len(options)} options)")
