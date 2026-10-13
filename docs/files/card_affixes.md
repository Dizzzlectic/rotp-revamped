# Card prefixes and suffixes

## Purpose

Supplies the prefixes and suffixes added to equipment names when cards are
inserted, such as “Lucky Sword” and “Sword of Ares.” These labels do not change
loose card names, which come from the item-info table, or the cards' effects.

## Files

| Source                                            | Destination                         | Text supplied                    |
| ------------------------------------------------- | ----------------------------------- | -------------------------------- |
| `data/cardprefixnametable.txt` in `kRO/data.grf`  | `src/data/cardprefixnametable.txt`  | Card affix labels                |
| `data/cardpostfixnametable.txt` in `kRO/data.grf` | `src/data/cardpostfixnametable.txt` | IDs identifying suffix placement |

See [inventory.json](../../inventory.json) for coverage and
[sources.json](../../sources.json) for reviewed sources and file-specific source
notes.

## Translation decisions

Cards 4031, 4038 and 4039 use the established affixes “of Ares,” “of Health” and
“of Aristotle.” For 27287, use iRO's “of Luminant” despite ROenglishRE's “of
Liniment.” Retain “Fatasm” for 4269 because the references do not establish a
corrected spelling.

Leading “Of” becomes “of”; “Orb of” becomes “of” where kRO uses 오브, the
loanword for “of.”

For 27304 (헬스), use **Healthy**, as in ROenglishRE.
[Divine-Pride](https://www.divine-pride.net/database/item/27304) shows “Hell's”
when iRO is selected and “Health” in other regional views, including Global
Zero. The usual health loanword and HP recovery context support the health
reading, but Gravity's intended English spelling remains unconfirmed.

For 300666, use “of Bulgasari”: 불가사리 names the monster here, rather than
“starfish” or ROenglishRE's “Buddha.”

## File format and client behavior

Name records have the form `card ID#label#`. The placement table contains
`card ID#` records for suffixes. Labels beginning with “of ” or “from ” follow
the equipment name; other labels precede it. Thus “of Health” renders as “Shoes
of Health,” while “Healthy” renders as “Healthy Shoes.” Both files are supplied
so placement agrees in Korean client text and English translation mode,
including newer kRO cards absent from iRO.

Name-table IDs, record order, duplicates and `#` delimiters are preserved.
Regional names can distinguish cards with identical Korean labels. The placement
table retains surviving kRO suffix IDs in source order and appends English
suffix IDs in name-table order. Source IDs 4495 and 4496 remain in the placement
table even though kRO supplies no corresponding name records.

Both replacements contain ASCII text without a BOM and use CRLF line endings.
Their bytes are identical in UTF-8 and CP949.
