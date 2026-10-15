# Skill names

## Purpose

Supplies names displayed in the skill interface. This table also contains skill
resources, levels, costs, ranges and prerequisites; translation changes only its
`SkillName` fields. Skill descriptions are a separate target.

## Files

| Source                                                                      | Destination                                                   | Text supplied |
| --------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------- |
| `data/luafiles514/lua files/skillinfoz/skillinfolist.lub` in `kRO/data.grf` | `src/data/luafiles514/lua files/skillinfoz/skillinfolist.lub` | Skill names   |

See [inventory.json](../../inventory.json) for coverage and
[sources.json](../../sources.json) for source versions, hashes and references.

## Translation decisions

Names follow kRO meaning, using matching iRO and ROenglishRE names as references.
Regional aliases are compared by the symbolic skill key and Korean name, rather
than copied by numeric ID alone. “Frost Joke” and “Scream” match the existing
[skill dialogue](skill_shouts.md). Recall destinations match the map names.

Monster skill labels retain source distinctions even where identifiers suggest
a different name: `NPC_COMET` is “Meteor Shower,” `NPC_JACKFROST` is “Frost
Piercing,” and `NPC_SATURDAY_NIGHT_FEVER` is “Friday Night Fever.”

Newer skills absent from the English references are translated from kRO.
[Gravity's developer note](https://ro.gnjoy.com/news/devnote/View.asp?category=3&curpage=1&seq=4200579)
provides context for the 2026 additions. `SKE_SEVENTH_KICK_S` is “Empowered Seven
Star Heavenly Kick,” using the documented stronger form rather than guessing
the final Korean syllable's character. `SOA_FIELD_OF_KIRIN` is “Yellow Dragon
Formation”: its Korean name and
[official description](https://ro.gnjoy.com/guide/runemidgarts/skillview.asp?lineseq=8&skillid=6637)
identify the Yellow Dragon rather than a kirin. These English names are project
translations, rather than claims of official regional spellings.

`EL_ICE_NEEDLE` contains the incomplete Korean label `아이스` (“Ice”), with a
trailing space.
“Ice Needle” restores the name supported by both English references and the
matching symbolic skill key; the complete wording is absent from this kRO field.

## File format and client behavior

The kRO source is compiled Lua 5.1. The replacement is readable Lua source with
ASCII text, CRLF line endings and no BOM. Its bytes work in both CP949 and UTF-8.

`SKILL_INFO_LIST` retains the original record order and `SKID`/`JOBID` references.
Resource names, levels, SP and AP costs, ranges, skill scales, prerequisites,
booleans and omitted fields retain the source values. No replacement enum table
is shipped. Newer and unused source entries remain in the complete table.

The client loads `skillid.lub` and skill descriptions before this table. It
registers each name and the accompanying metadata through `AddSkillInfo`.
