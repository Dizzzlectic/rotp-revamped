# Card prefixes and suffixes

The source is `data/cardprefixnametable.txt` inside `kRO/data.grf`. The mod
replaces it at `src/data/cardprefixnametable.txt`. All 1,349 records are
translated, covering 1,339 card IDs and 1,275 distinct source labels. The ten
repeated records are preserved in their original positions.

These labels appear on equipment containing cards, such as “Lucky Sword” or
“Sword of Mars.” They do not change the names of loose cards, which come from
the item-info table.

## Placement and wording

Each record has the form `card ID#label#`. Despite the filename, the table
contains both prefixes and suffixes. `data/cardpostfixnametable.txt` lists the
IDs whose labels follow the equipment name; all other labels precede it. That
numeric table is checked alongside the translation and remains unchanged in
the base client.

Korean adjectives and possessives become English modifiers suitable for their
position. Loanwords retain their meaning, and named characters retain their
names. iRO and ROenglishRE supply references where their wording agrees with
kRO; different meanings and misspellings are not carried over. kRO's
`NPCIdentity` keys supply Latin spellings for newer monster names where
available. Unconfirmed spellings for coined labels are recorded by card ID in
`sources.json`.

The following Korean labels become the English labels in the replacement:

| Card ID | Korean source | English        |
| ------- | ------------- | -------------- |
| 4001    | 럭키          | Lucky          |
| 4031    | 오브 마르스   | of Mars        |
| 4038    | 회복의        | Restorative    |
| 4039    | 아리스토의    | Aristotle's    |
| 4079    | 오브 파워     | of Power       |
| 4421    | 치누크        | Chinook        |
| 4472    | 카니발        | Carnival       |
| 27180   | 파워 브레이크 | Power Break    |
| 27304   | 헬스          | Health         |
| 300013  | 레긴레이브    | Reginleif      |
| 300666  | 오브 불가사리 | of Bulgasari   |
| 300761  | 오브 용지락   | of Dragon Clam |

“Mars” preserves the named deity rather than changing it to “Ares.”
“Carnival” follows the Korean loanword rather than substituting “Carnivore.”
Bulgasari is the named monster here, rather than the other meaning of the
Korean word, “starfish.”

## File format

The replacement is plain text stored as UTF-8 without a BOM, with CRLF line
endings. Its English labels use only ASCII characters, whose bytes also decode
correctly as CP949 under the Korean client setting. Card IDs and `#`
delimiters are preserved.
