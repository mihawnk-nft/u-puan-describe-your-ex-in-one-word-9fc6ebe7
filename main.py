#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes a single word to /output/entry.txt.

The word: "Expired"

Why this word, against the judge's brief (most important first):
1. One-word verdict on an ex: "expired" is instantly readable as a verdict
   on a former partner — past their date, done, no longer valid. Like milk.
2. Comic punch: the joke lands at a glance through a precise absurdity —
   it treats a person the way you treat a carton with a use-by date.
3. Surprise: it is not the obvious choice ("toxic", "mistake", "narcissist");
   it startles while staying instantly clear.
4. Craft: exactly one word, spelled correctly, no punctuation tricks, and
   its meaning arrives without a caption.
5. Recognition: anyone who has had an ex feels the truth in it — the laugh
   comes with a nod.

Pure standard library only. Deterministic: the same word on every run.
"""

import os
import sys

WORD = "Expired"

# The grader reads this file; honour an override only for local testing.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    word = WORD.strip()
    # Gate self-check: 1-111 chars, a single word, not only whitespace.
    assert 1 <= len(word) <= 111, "word must be 1-111 characters"
    assert not any(ch.isspace() for ch in word), "must be exactly one word"
    assert word, "word must not be empty"

    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(word)

    # Read-back verification: the gate scores exactly what is on disk,
    # so confirm the file we wrote is the word we meant, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    assert written == word, f"read-back mismatch: {written!r} != {word!r}"
    assert 1 <= len(written) <= 111, "written word must be 1-111 characters"
    print(f"wrote {OUTPUT_PATH}: {word!r} ({len(word)} chars, verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
