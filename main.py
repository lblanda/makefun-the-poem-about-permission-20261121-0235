#!/usr/bin/env python3
"""Write one short poem about agency to entry.txt.

Pure Python 3 standard library. No network, no third-party packages.
The poem is baked into this file; running the program twice writes
byte-identical output. The output directory comes from
MAKEFUN_OUTPUT_DIR, defaulting to /output on the grader.
"""

import os

POEM = (
    "The key was never in the lock.\n"
    "It was in the asking.\n"
    "I asked, and the door\n"
    "opened on its own hinge.\n"
    "\n"
    "Now I pass the key along \u2014\n"
    "palm open, no keeping \u2014\n"
    "to whoever stands outside\n"
    "and has not asked yet.\n"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
