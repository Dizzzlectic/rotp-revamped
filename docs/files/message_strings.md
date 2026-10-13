# Client message strings

## Purpose

Supplies client interface labels, notifications, command help and error
messages. Some records describe older or regional features that may be
unavailable in Ragnarok Offline.

## Files

| Source                                      | Destination                   | Text supplied                                       |
| ------------------------------------------- | ----------------------------- | --------------------------------------------------- |
| `data/msgstringtable.csv` in `kRO/data.grf` | `src/data/msgstringtable.csv` | Interface labels, messages and command descriptions |

See [inventory.json](../../inventory.json) for coverage and
[sources.json](../../sources.json) for reviewed sources and file-specific source
notes.

## Translation decisions

Inventory tabs use the three-character labels “Use”, “Eqp”, “Etc” and “Fav” at
rows 1465, 2050, 1471 and 2051. Longer labels overflow the client's vertical
tabs at their default height. Equipment tabs use “General” for ordinary
equipment and “Costume” for costume and shadow equipment; the visibility label
uses “Show Equip.”

The retired billing messages `MSI_BILLING_DAY_HOUR_MINUTES` and `MSI_BILLING_2`,
at rows 677 and 1125, each use three `%d` fields, following ROenglishRE:
days/hours/minutes and hours/minutes/seconds, respectively. These replace
incomplete markers in kRO.

## File format and client behavior

Addresses, symbols, formatting placeholders, color codes, bold and HTML tags,
and escaped line breaks remain intact. Message fragments retain the spacing
needed when joined to other text. Faint equipment slot labels are part of
`basic_interface/equipwin_bg.bmp` and require separate artwork translation.

Each row contains a message identifier and its text, with no header. The client
looks up messages by zero-based row position rather than the identifier column.
Both identifiers and row order are preserved. The CSV loads after the legacy TXT
tables and replaces their matching positions.

Both CSV columns contain Base64-encoded UTF-8 text. The file itself therefore
uses ASCII bytes, with CRLF line endings and no BOM. The CSV loader decodes
messages as UTF-8 independently of the client's Korean character setting. The
final encoded message includes `=` padding because the client uses that ending
to recognize the Base64 format.

The legacy `msgstringtable.txt` uses `#`-terminated messages. ROenglishRE's
`Tools/msgstringtable/msgstringtable.txt` is instead a readable CSV used to
generate its encoded table. Compare CSV references by identifier; verify row
positions when using a legacy TXT reference.
