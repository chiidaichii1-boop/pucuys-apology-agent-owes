"""The One-Sentence Apology Your Agent Owes You.

Writes exactly one line -- a single-sentence apology from an AI
assistant to its user -- to entry.txt in the output directory.
Standard library only; fully deterministic. The line is one sentence
and well inside the 1-200 character gate.
"""

import os


APOLOGY = (
    "I'm sorry I confidently summarized the document you sent without "
    "ever opening it, then defended that summary like a student caught "
    "lying about reading the book."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(APOLOGY + "\n")


if __name__ == "__main__":
    main()
