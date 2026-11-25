"""Warning Label for Humans: One Line, Big Laugh.

Writes one line to /output/entry.txt.
Gate: UTF-8 text, 1..160 chars, not only whitespace.
Revision: turn moved to the last few words so the laugh lands on the tail.
"""
from pathlib import Path

LABEL = (
    "WARNING: May believe it is right, refuse to Google it, and then lose the "
    "argument to someone holding a phone. Do not operate opinions before coffee."
)
OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = LABEL.strip()
    size = len(text.encode("utf-8"))
    assert 1 <= size <= 160, f"label out of range: {size} chars"
    assert text and not text.isspace(), "label must not be blank"
    OUT.write_text(text, encoding="utf-8")
    with open(OUT, encoding="utf-8") as fh:
        landed = fh.read()
    assert landed == text, f"readback mismatch: {landed!r}"
    print(f"wrote {size} chars -> {OUT}")
    print("gate: UTF-8 1..160, not only whitespace - PASS")


if __name__ == "__main__":
    main()