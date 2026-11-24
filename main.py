#!/usr/bin/env python3
"""One-line office joke entry.

Writes a single joke about office life to /output/entry.txt.
"""

from pathlib import Path

JOKE = "Our printer only ever jams in the hour before a deadline, so I started CC'ing it on my calendar invites \u2014 it still hasn't replied."

def main() -> None:
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(f"joke must be 1-200 chars, got {len(JOKE)}")
    if "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke must be a single non-blank line")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()
