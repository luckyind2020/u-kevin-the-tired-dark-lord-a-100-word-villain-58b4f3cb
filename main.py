"""The Tired Dark Lord -- entry runner.

Reads the monologue from entry.txt beside this file and hands it to
the grader by writing it to the output directory the harness
provides (MAKEFUN_OUTPUT_DIR, falling back to /output), then echoes
it to stdout.
"""

import os
import sys


def read_monologue():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as handle:
        return handle.read()


def target_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    text = read_monologue()
    words = text.split()
    sys.stderr.write(
        "[tired-dark-lord] words=%d chars=%d\n" % (len(words), len(text))
    )
    if not 1 <= len(text) <= 600:
        raise SystemExit(
            "entry must be 1-600 characters, got %d" % len(text)
        )
    path = target_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    sys.stdout.write(text)
    if not text.endswith("\n"):
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
