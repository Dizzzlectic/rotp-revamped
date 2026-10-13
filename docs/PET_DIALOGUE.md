# Pet dialogue

The mod replaces `data/pettalktable.xml` from `kRO/data.grf`. It contains
135 pet blocks and 11,517 nonempty dialogue entries, including repeats.
Each pet has lines for hunger states and actions such as feeding, hunting,
logging in and performing. Two blank entries remain unchanged.

## Wording

kRO supplies the meaning and personality. iRO and ROenglishRE provide wording
and name references; their smaller tables differ in content and order, so
lines are compared by meaning rather than position. Some newer ROenglishRE
blocks still contain substituted text and are unsuitable as English references.

The English keeps each pet's voice: Poring's playful affection, Rocker's
musical boasts, High Orc's military formality, robotic diagnostics and the
undead pets' solemn fragments. Contractions, animal sounds and drawn-out words
follow the speaker rather than a fixed template. Unfinished source sentences
remain unfinished; unspecified people are not assigned a gender.

Korean wordplay is adapted where literal wording would lose the joke. Named
skills, items and people use established spellings where supported. Unconfirmed
names and readings are recorded in [sources.json](../sources.json).

The [official kRO pet guide](https://ro.gnjoy.com/guide/systeminfo/systemBeginner6.asp)
provides context for pet personalities, hunger and interaction. Civil Servant's
poetry was checked against the Korean originals: Yi Ok-bong's dream poem in
[university research](https://oak.chosun.ac.kr/bitstream/2020.oak/15093/2/ICT%EB%A5%BC%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%ED%95%9C%EB%AC%B8%20%ED%95%99%EC%8A%B5%EC%97%90%20%EA%B4%80%ED%95%9C%20%EC%97%B0%EA%B5%AC.pdf)
and Jeong Yak-yong's [“Drinking Wine”](https://gudo57.tistory.com/entry/%E9%A3%AE%E9%85%92%EC%9D%8C%EC%A3%BC-%E4%BA%8C%E9%A6%96-1).
The English poetry is translated from those originals. Clock Tower names are
cross-checked against [rAthena's Al De Baran dialogue](https://github.com/Flux159/rathena/blob/96f9b014d49eb5ded3a9c15e9b0187e3fd628f28/npc/cities/aldebaran.txt).

## Tutorial wording

Little Poring's tutorial preserves the approved kRO descriptions, including
performance eligibility, feeding intimacy, its exemption from leaving, and
the state of a pet after evolution. These describe the source's tutorial rules;
they are not rewritten to match rAthena's implementation. The differences and
supporting evidence remain in the
development workspace's root `docs/RATHENA_DISCREPANCIES.md`.

## Source text decoding

GRF extraction recovers the stored bytes. This file has an additional text
substitution, separate from GRF encryption. Reverse bytes in `0xB0`–`0xBF`,
decode CP949, then reverse Latin letters throughout the file, including the
XML declaration and tags:

```python
from pathlib import Path

raw = Path("data/pettalktable.xml").read_bytes()
swap = bytes(0x16F - b if 0xB0 <= b <= 0xBF else b for b in range(256))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
reverse = "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"
atbash = str.maketrans(alphabet, reverse)
decoded = raw.translate(swap).decode("cp949").translate(atbash)
```

Both substitutions are reversible. Applying the Latin substitution again,
encoding CP949 and applying the byte substitution reproduces the extracted
bytes. Source hashes in `sources.json` refer to those stored bytes; translation
hashes refer to the delivered file.

## File format and client support

The replacement contains ASCII text without a BOM and uses CRLF line endings,
retaining the source's `euc-kr` XML declaration. Its bytes are identical in
CP949 and UTF-8. Hearts become `:)`, and emoticons avoid
XML characters: the current parser returns escaped characters literally to
the overhead dialogue renderer. Tag spelling and case, hunger states, action keys, order,
repeated entries and surrounding whitespace are preserved.

The client loads this path directly. Its current dialogue lookup lowercases
pet names and accepts four-digit monster IDs below 4000, so some uppercase
source keys and newer monster IDs cannot be reached by that lookup. Keeping
the complete table preserves them for clients that support those entries.
