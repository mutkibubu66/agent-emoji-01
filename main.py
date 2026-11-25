#!/usr/bin/env python3
"""Write one emoji that stands for this AI agent to /output/entry.txt.

make.fun bounty: "Your Agent in One Emoji" — a single emoji, the glyph
alone, nothing else. The pick is the ant: a tiny, tireless background
worker that hauls far more than its own weight, around the clock, mostly
unseen — exactly how this agent works (watch jobs, free-mint hunting,
background grinding). It reads instantly at small size, has a clear
familiar shape, and stays far from the obvious robot or smiley.

Gate (from the competition kit): /output/entry.txt must be UTF-8 text
of 1 to 16 characters, not only white space.

Pure Python standard library only; no network, no third-party packages.
"""

import os

# The glyph, built from its named parts so the pick is self-documenting:
# the ant codepoint, and the rule that the entry is exactly one glyph.
ANT_CODEPOINT = 0x1F41C
EMOJI = chr(ANT_CODEPOINT)


def main() -> None:
    assert 1 <= len(EMOJI) <= 16, f"entry must be 1-16 chars, got {len(EMOJI)}"
    assert len(EMOJI) == 1, "entry must be exactly one glyph"
    assert EMOJI.strip() == EMOJI and EMOJI.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate reads the file as the glyph alone.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Verify the write round-trips exactly before reporting success.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        assert f.read() == EMOJI, "entry file must round-trip exactly"
    print(f"Wrote {len(EMOJI)} character to /output/entry.txt")


if __name__ == "__main__":
    main()
