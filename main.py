#!/usr/bin/env python3
"""Entry program for make.fun bounty: news-image-20261124
"Sum up 24 November's world news in one image"

The simplest valid program shape for image bounties on make.fun:
copy the image bundled in the repository to /output/entry.png,
byte for byte. Standard library only, no network access, and two
runs always write identical bytes (the harness requirement).

Layout expected by the bounty:
  main.py    <- this file, at the repository root (Python 3.13)
  entry.png  <- 1024x1024 PNG, 552,709 bytes (limit: 1 MiB)
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main() -> None:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
