#!/usr/bin/env python3
"""Prose fingerprint — measures a book's sentence-level cadence.

Usage:
    python3 prose_fingerprint.py <file.html|file.txt> [--json]

Reports, per ~1000 words of prose:
  - sentence length: mean and standard deviation (words)
  - em-dash frequency (per 1000 words)
  - colon frequency (per 1000 words)
  - aphorism ratio: share of sentences with <= 6 words
  - long-sentence ratio: share of sentences with >= 25 words

Why: the structural digest catches skeletons and headings; this catches the AUTHOR'S
HAND — the punchy-aphorism-plus-em-dash-pivot house cadence that bleeds through
otherwise different brand registers. Each book's author profile
(references/author_synthesis.md) declares target bands; the book must land inside its
own author's bands AND outside the immediately previous book's measured values on at
least two metrics. Compare against the PROSE FINGERPRINT lines in
references/structural_digests.md.

Heuristics: strips HTML tags, drops heading-like lines (short, no terminal punctuation,
or letter-spaced), splits sentences on ./!/? followed by whitespace+capital. Good enough
for comparison; not a linguistics engine — always compare fingerprints computed by this
same script.
"""
import json
import re
import statistics
import sys


def extract_prose(raw: str) -> str:
    # strip script/style blocks then tags
    raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
    raw = re.sub(r"<[^>]+>", "\n", raw)
    lines = []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        # drop letter-spaced headings ("R O L E X", "T H E  M A R K")
        tokens = line.split()
        if len(tokens) >= 4 and sum(len(t) == 1 for t in tokens) / len(tokens) > 0.6:
            continue
        # drop short heading-like lines without terminal punctuation
        if len(tokens) <= 5 and not re.search(r"[.!?]$", line):
            continue
        lines.append(line)
    return " ".join(lines)


def fingerprint(text: str) -> dict:
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", text)
    n_words = len(words)
    if n_words < 200:
        raise SystemExit("Too little prose (<200 words) for a stable fingerprint.")
    # sentence split
    sentences = re.split(r"(?<=[.!?])\s+(?=[\"'“”A-Z0-9])", text)
    lengths = []
    for s in sentences:
        w = re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", s)
        if 1 <= len(w) <= 120:
            lengths.append(len(w))
    per_k = 1000.0 / n_words
    em_dashes = text.count("—") + text.count(" -- ")
    colons = len(re.findall(r":\s", text))
    return {
        "words_analyzed": n_words,
        "sentences": len(lengths),
        "sentence_mean": round(statistics.mean(lengths), 1),
        "sentence_stdev": round(statistics.pstdev(lengths), 1),
        "em_dash_per_1000w": round(em_dashes * per_k, 1),
        "colon_per_1000w": round(colons * per_k, 1),
        "aphorism_ratio": round(sum(1 for x in lengths if x <= 6) / len(lengths), 2),
        "long_sentence_ratio": round(sum(1 for x in lengths if x >= 25) / len(lengths), 2),
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    with open(sys.argv[1], encoding="utf-8", errors="ignore") as f:
        fp = fingerprint(extract_prose(f.read()))
    if "--json" in sys.argv:
        print(json.dumps(fp, indent=2))
    else:
        for k, v in fp.items():
            print(f"{k:>22}: {v}")
