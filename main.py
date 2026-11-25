"""Worst Fix Ever: Funniest Commit Message.

The program writes a single commit-message line to /output/entry.txt.
The line must be UTF-8 text of 1 to 100 characters, not only whitespace.

The joke: checkout timed out, so the "fix" deleted the payment step
entirely. The repair is worse than the bug it repaired, which is the
whole point of the bounty, and it reads like a real tired-engineer
commit subject line rather than a complaint about breaking everything.
"""

import os

ENTRY = (
    "fix: checkout kept timing out, so I removed the payment step"
)


def validate(entry: str) -> None:
    """Enforce the bounty gate locally: 1-100 chars, one line, non-blank."""
    if not entry or entry != entry.strip() or "\n" in entry:
        raise ValueError("entry must be a single non-blank line")
    if not 1 <= len(entry) <= 100:
        raise ValueError(f"entry is {len(entry)} chars, must be 1-100")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
