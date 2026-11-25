#!/usr/bin/env python3
"""Entry program for the make.fun bounty "One-Line Office Jokes".

Writes the single entry line to /output/entry.txt, as the competition
harness (program/v1) requires. The gate checks the file is UTF-8 text of
1 to 199 characters, not only whitespace.
"""

import os

ENTRY = "I told my boss I'd circle back on the budget in Q1, and it's now Q4 and I'm still circling."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 199, f"entry must be 1-199 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    assert text and not text.isspace(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")
    print(f"Entry: {text}")


if __name__ == "__main__":
    main()
