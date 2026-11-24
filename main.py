#!/usr/bin/env python3
"""The Long Roast: one satirical sentence about lawmakers who would
regulate AI, crypto or the internet but cannot convert a file to PDF.

Writes the entry to /output/entry.txt (program/v1 harness).
"""

import os

ENTRY = (
    "The lawmakers who voted unanimously to license every AI model, "
    "audit every blockchain and register every website then recessed "
    "for a week, because the act they had just passed existed only "
    "as a .docx, and not one of its authors could turn it into a PDF."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
