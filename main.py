#!/usr/bin/env python3
"""Make the AI Judge Laugh entry.

Writes exactly one funny line about office life to /output/entry.txt
(1-200 UTF-8 chars, not only whitespace), as the sealed scorer's gate
requires. Deterministic, stdlib only, no network, no secrets, no
randomness.

The joke targets the judge's brief in order: it is plainly about office
life (the printer), the observation is true (printers jam and complain
at the worst moment), the turn is surprising (the complaint itself
burns the resource it claims to lack), it is tight (one breath, the
twist lands on the last three words), and the angle is fresh — the
machine, not the worker, is the one misbehaving.
"""

import os

ENTRY = "I told the printer it was out of ink, so it printed a 40-page error report about being out of ink."


def validate(entry):
    """Gate self-check: the sealed scorer requires /output/entry.txt to
    be UTF-8 text of 1 to 200 characters, not only whitespace. Fail
    loudly here instead of shipping a rejected entry."""
    assert 1 <= len(entry) <= 200, f"entry length {len(entry)} outside 1-200"
    assert "\n" not in entry and "\r" not in entry, "entry must be one line"
    assert entry == entry.strip(), "entry has leading/trailing whitespace"
    assert all(ord(c) >= 32 for c in entry), "entry has control characters"


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back byte-for-byte: what is on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "read-back mismatch"


if __name__ == "__main__":
    main()
