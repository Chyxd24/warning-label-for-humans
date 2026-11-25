#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes one line to /output/entry.txt.
Gate: UTF-8 text, 1..160 chars, not only whitespace.
Revision: label tightened to land the turn in the last words (138 chars).
"""
from pathlib import Path

LABEL = (
    "WARNING: Prolonged exposure to your own thoughts may cause you to believe "
    "you were right all along. Discontinue use if certainty persists."
)
OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = LABEL.strip()
    size = len(text.encode("utf-8"))
    assert 1 <= size <= 160, f"label out of range: {size} chars"
    assert text and not text.isspace(), "label must not be blank"
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {size} chars -> {OUT}")
    print("gate: UTF-8 1..160, not only whitespace - PASS")


if __name__ == "__main__":
    main()