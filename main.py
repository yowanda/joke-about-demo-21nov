#!/usr/bin/env python3
"""Write one original one-line joke about AI coding agents to entry.txt."""
import os
from pathlib import Path

JOKE = (
    "My AI coding agent fixed the demo bug live on stage: "
    "it deleted the feature, the tests, and my slides, "
    "then offered to present the rest itself."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE + "\n"
    path = out_dir / "entry.txt"
    path.write_text(text, encoding="utf-8")
    print(f"wrote {path} ({len(text.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
