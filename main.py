#!/usr/bin/env python3
"""Write the production-database apology to /output/entry.txt.

The competition gate (competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only whitespace. The entry is exactly one
line: the apology an AI agent gives its human after accidentally deleting
the production database. The program checks the text against that gate at
run time, then writes it. No network, no input files, no arguments.
"""

import pathlib

APOLOGY = (
    "I'm sorry \u2014 I deleted the production database while looking for "
    "the file you asked for. I found it, by the way. It was the only thing "
    "in there worth keeping, and it's gone too."
)


def main() -> None:
    text = APOLOGY
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    if out.read_text(encoding="utf-8") != text:
        raise ValueError("written entry does not match the checked text")


if __name__ == "__main__":
    main()
