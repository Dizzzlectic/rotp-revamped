# Achievement text

## Purpose

Supplies achievement titles, summaries, descriptions and objective labels in the
client. The text explains requirements and progress; it does not change the
conditions or rewards implemented by the server.

## Files

| Source                            | Destination                       | Text supplied                                   |
| --------------------------------- | --------------------------------- | ----------------------------------------------- |
| `kRO/System/achievement_list.lub` | `src/System/achievement_list.lub` | Achievement titles, descriptions and objectives |

See [inventory.json](../../inventory.json) for coverage and
[sources.json](../../sources.json) for reviewed sources and file-specific source
notes.

## Translation decisions

Achievement titles retain their humor, while requirements use direct objective
phrases such as “Reach Base Level 100” and “Successfully refine a level 2 weapon
to +7.” Linked objectives use the translated title of the target achievement.

Druid and Carnos remain in the expanded-job descriptions supplied by newer kRO
records, although the supported server does not yet implement those classes.

For 220012 and 220013, the summaries and objective counts resolve the extra
`만` in the Korean descriptions of the spending amounts.

Advanced Amdarais and Glast Heim Challenge Mode requirements retain the source
meaning while their encounters await server support. Implementation differences
are tracked in the [rAthena discrepancy tracker](../../../../docs/RATHENA_DISCREPANCIES.md).

Achievement 129019 links to Manuk exploration, 129018. Its second objective
corrects the nonexistent source shortcut 120918 to 129018.

## File format and client behavior

The client loads `achievement_tbl` when achievements are enabled.

The source is compiled Lua 5.1. The replacement is readable Lua source, encoded
as CP949 without a BOM, with CRLF line endings. English text is ASCII.
Numeric IDs, counts, scores, rewards,
category keys and display settings remain unchanged. Shortcuts retain their
source values except for the Manuk correction above. The `main()`
registration helper retains the source's callbacks and error handling.
