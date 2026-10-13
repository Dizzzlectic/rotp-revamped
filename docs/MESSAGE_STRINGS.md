# Client message strings

The source is `data/msgstringtable.csv` inside `kRO/data.grf`. The mod replaces
it at `src/data/msgstringtable.csv`.

## Lookup and wording

Each row contains a message identifier and its text. There is no header. The
client looks up messages by zero-based row position, rather than by the
identifier column. Both identifiers and row order are preserved. The CSV loads
after the legacy TXT message tables and replaces their matching positions.

These examples show decoded cells from the source and replacement:

| Row  | Identifier                     | Korean source                                 | English                                             |
| ---- | ------------------------------ | --------------------------------------------- | --------------------------------------------------- |
| 487  | `MSI_GOT_EXPERIENCE_POINT`     | 경험치 %d 얻음                                | Gained %d experience                                |
| 488  | `MSI_GOT_JOB_EXPERIENCE_POINT` | 잡경험치 %d 얻음                              | Gained %d Job experience                            |
| 3730 | `MSI_IQ_SINCERE_FAITH_ON`      | 공격 속도 및 유도 공격 확률이 증가되었습니다. | Attack speed and Perfect Hit chance have increased. |

The table includes messages for older and regional client features, which may
be unavailable in Ragnarok Offline. Existing English text is reviewed alongside
newly translated text; addresses and symbols remain intact.
Command spellings follow the English references, with supported client commands
checked against roBrowserLegacy. The descriptions retain kRO's meaning.

Inventory tabs use ROenglishRE's three-character labels “Use”, “Eqp”, “Etc”
and “Fav”, at rows 1465, 2050, 1471 and 2051, respectively. These agree between
its Renewal TXT and compatibility CSV tables. iRO uses “Item”, “Gear”, “Etc.”
and “Fav”; its four-character labels are too tall for the client's current
vertical tabs at their default height.

Equipment tabs use “General” for ordinary equipment and “Costume” for costume
and shadow equipment. “General” replaces `일반 장비` at rows 1805 and 3158;
“Costume” replaces `특수 장비` at row 3159, matching ROenglishRE. The faint slot labels inside the
equipment panel are printed in `basic_interface/equipwin_bg.bmp`, including its
“accessary” spelling, and are a separate artwork target. The equipment visibility
label at row 1362 uses “Show Equip”, as in iRO and ROenglishRE's compatibility
CSV table. ROenglishRE's Renewal TXT uses “Show Equipment”.

Stat labels and numeric bonuses use `Critical` for critical hit chance and
uppercase abbreviations such as `MATK`, `MDEF`, `HIT`, `FLEE` and `ASPD`.
Explanations use consistent full names,
including “critical hit chance,” “accuracy” and “evasion,” as defined in the
[terminology reference](TERMINOLOGY.md).

Formatting placeholders, color codes, bold and HTML tags, and escaped line
breaks are preserved. Message fragments retain the spacing needed when joined
to names or other text. The retired account-time billing messages
`MSI_BILLING_DAY_HOUR_MINUTES` and `MSI_BILLING_2`, at rows 677 and 1125, each use
three `%d` fields, as in ROenglishRE: days/hours/minutes and hours/minutes/seconds,
respectively. This restores incomplete markers in the Korean source.

## File format

Both CSV columns contain Base64-encoded UTF-8 text. The file itself therefore
uses ASCII bytes, with CRLF line endings and no BOM. The CSV loader decodes
the messages as UTF-8 independently of the client's Korean character setting.
The final encoded message includes `=` padding because the client uses that
ending to recognize the Base64 format.

The legacy `msgstringtable.txt` uses `#`-terminated messages. ROenglishRE's
`Tools/msgstringtable/msgstringtable.txt` is instead a readable CSV used to
generate its encoded table. Reference tables differ in coverage: compare CSV
entries by identifier and verify row positions when using a legacy TXT table.
