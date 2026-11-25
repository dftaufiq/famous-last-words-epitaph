#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — make.fun entry.

Writes the funniest one-line famous last words, a tombstone epitaph of at
most 150 characters, to /output/entry.txt. Deterministic: the same line
every run, no network, no secrets, no input read from anywhere.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-150 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 150:
        print(f"ERROR: entry is {len(line)} chars, over the 150-char limit",
              file=sys.stderr)
        sys.exit(1)


def verify_written(path: str, line: str) -> None:
    """Round-trip check: the file on disk must be byte-for-byte the line.

    Fails loudly (non-zero exit) so a truncated or altered write never
    ships silently.
    """
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print(f"ERROR: {path} does not match the entry line "
              f"({len(written)} chars written, {len(line)} expected)",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "I died doing what I loved: ignoring the check-engine light for "
    "14 months. The car is fine. I am not."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    verify_written(path, LINE)
    print(LINE)


if __name__ == "__main__":
    main()
