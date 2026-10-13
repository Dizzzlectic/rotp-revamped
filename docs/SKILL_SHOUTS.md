# Frost Joke and Scream dialogue

The mod replaces `data/ba_frostjoke.txt` and `data/dc_scream.txt` from
`kRO/data.grf`. These lines are spoken when using Frost Joke and Scream;
they do not change either skill's effects.

| File               | Dialogue lines | Heading            | Nonempty text records |
| ------------------ | -------------- | ------------------ | --------------------- |
| `ba_frostjoke.txt` | 118            | `FROST JOKE`       | 119                   |
| `dc_scream.txt`    | 116            | `Dancer's Scream!` | 117                   |

kRO supplies the content and tone. iRO and ROenglishRE provide reference
phrasing and established names, but their tables differ from kRO in both
content and order. Entries are compared by meaning rather than row number.
The source versions and hashes are recorded in [sources.json](../sources.json).

## Wording

Frost Joke keeps its deliberately bad puns, monster names, distorted spell
names and absurd boasts. Korean wordplay becomes an English equivalent where
a literal translation would lose the joke. For example:

| Source dialogue line | Korean wordplay or meaning                              | English adaptation                                                                |
| -------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Frost Joke 1         | Tristan III treated as a third installment              | “Tristan III? Were the first two any good?”                                       |
| Frost Joke 20        | SARS and Sasquatch                                      | “I think I've caught SARS-quatch!”                                                |
| Frost Joke 87        | A declaration of love turns into talk of pancake batter | “High Priest, you're my batter half! Speaking of batter, can you flip a pancake?” |
| Frost Joke 97        | Healing and high heels                                  | “P-Priest... h-heal me... or just lend me those high heels!”                      |
| Frost Joke 113       | Money and Grandma                                       | “What's worth more than a grand to Grandpa? Grandma!”                             |

Scream retains its exaggerated anger, crying, affection and melodrama.
Unspecified people remain unspecified; romantic uses of `오빠` become
“Sweetheart,” while `언니` retains “big sis.” Drawn-out sounds and hearts use
ASCII spellings such as `Aaaah!` and `<3`.

Scream line 114 mixes “Am I pretty?” with the ending of Frost Joke's Elder
counting line. The translation keeps both parts rather than substituting
iRO's different ending. The isolated syllable `리`, left from the counting
phrase, has no standalone English meaning and is omitted.

## Source text decoding

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

## File format

Both replacements contain ASCII text without a BOM, with CRLF line endings.
Their bytes are identical in CP949 and UTF-8. Tabs separate records; newlines
alone do not. Record order, Frost Joke's empty field after dialogue line 8,
and its repeated closing lines are preserved.

Each replacement ends with a tab so the current client loader reads the final
record. The empty terminal field is not loaded and is excluded from progress.
The heading is loaded as a text record and is included in progress; Frost
Joke's interior empty field is excluded.
