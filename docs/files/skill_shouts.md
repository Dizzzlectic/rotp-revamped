# Frost Joke and Scream dialogue

## Purpose

Supplies the dialogue spoken when using Frost Joke and Scream. These lines carry
the skills' jokes and dramatic voices; they do not change skill effects.

## Files

| Source                                    | Destination                 | Text supplied       |
| ----------------------------------------- | --------------------------- | ------------------- |
| `data/ba_frostjoke.txt` in `kRO/data.grf` | `src/data/ba_frostjoke.txt` | Frost Joke dialogue |
| `data/dc_scream.txt` in `kRO/data.grf`    | `src/data/dc_scream.txt`    | Scream dialogue     |

See [inventory.json](../../inventory.json) for coverage and
[sources.json](../../sources.json) for reviewed sources and file-specific source
notes.

## Translation decisions

Frost Joke line 20 combines SARS with Sasquatch as “SARS-quatch.” Line 87 adapts
a declaration of love and pancake batter into “you're my batter half.”

In Scream, romantic uses of `오빠` become “Sweetheart,” while `언니` retains
“big sis.” Drawn-out sounds and hearts use ASCII spellings such as `Aaaah!` and
`<3`.

Scream line 114 mixes “Am I pretty?” with the ending of Frost Joke's Elder
counting line. The translation keeps both parts rather than substituting iRO's
different ending. The isolated syllable `리`, left from the counting phrase, has
no standalone English meaning and is omitted.

## File format and client behavior

The first record is a heading: `FROST JOKE` or `Dancer's Scream!`.

Both replacements contain ASCII text without a BOM, with CRLF line endings.
Their bytes are identical in CP949 and UTF-8. Tabs separate records; newlines
alone do not. Record order, Frost Joke's empty field after dialogue line 8, and
its repeated closing lines are preserved.

Each replacement ends with a tab so the current client loader reads the final
record. The empty terminal field is not loaded and is excluded from progress.
The heading is loaded as a text record and is included in progress; Frost Joke's
interior empty field is excluded.

### Source text decoding

GRF extraction recovers these files' stored bytes. Their Korean text has an
additional substitution, separate from GRF encryption:

1. Reverse bytes in `0xB0`–`0xBF` with `0x16F - byte`; leave other bytes alone.
2. Decode the result as CP949.
3. Reverse Latin letters in the body (`A` ↔ `Z`, `a` ↔ `z`). Keep the first
   line's Latin letters unchanged.

This reproduces the readable source without replacing its jokes with another
region's table. Both substitutions are reversible. For either extracted file:

```python
from pathlib import Path

raw = Path("data/ba_frostjoke.txt").read_bytes()
swap = bytes(0x16F - b if 0xB0 <= b <= 0xBF else b for b in range(256))
text = raw.translate(swap).decode("cp949")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
reverse = "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"
atbash = str.maketrans(alphabet, reverse)
heading, newline, body = text.partition("\r\n")
decoded = heading + newline + body.translate(atbash)
```

The source hashes refer to the extracted, still-substituted bytes; translation
hashes refer to the delivered English files.
