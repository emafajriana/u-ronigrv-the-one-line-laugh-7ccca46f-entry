"""u-ronigrv-the-one-line-laugh-7ccca46f entry (Python 3.13, stdlib only).

The program writes one funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader), then verifies the
written file: UTF-8, a single sentence, 1-200 characters, not blank.
"""

import os
from pathlib import Path

LINE = (
    "I forgot my password manager's master password, so now it's written "
    "on a sticky note stuck to my monitor."
)

OUTPUT_NAME = "entry.txt"


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / OUTPUT_NAME


def check_line(line: str) -> None:
    """Raise ValueError unless the line passes the competition gate."""
    if not line or not line.strip():
        raise ValueError("line is empty")
    if len(line) > 200:
        raise ValueError(f"line is {len(line)} characters, over the 200 limit")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must be a single sentence")
    line.encode("utf-8")


def write_entry() -> Path:
    """Write the line and verify it by reading it back."""
    check_line(LINE)
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE + "\n", encoding="utf-8")
    read_back = path.read_text(encoding="utf-8")
    if read_back != LINE + "\n":
        raise ValueError("read-back mismatch")
    return path


def main() -> None:
    """Write the entry and report its length."""
    path = write_entry()
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
