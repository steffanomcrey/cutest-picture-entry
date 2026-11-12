#!/usr/bin/env python3
"""make.fun entry: cutest-picture-01.

Ships one finished picture (artwork.png, created for this competition) and
writes it byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png (default
/output/entry.png). The competition's Deliverables bless this exact shape:
"the simplest program copies an image the repository holds". No inputs, no
network; identical bytes on every run.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASSET = HERE / "artwork.png"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(ASSET, target)
    written = target.stat().st_size
    expected = ASSET.stat().st_size
    if written != expected:
        raise SystemExit(f"copy truncated: wrote {written} of {expected} bytes")
    print(f"entry.png: {written} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
