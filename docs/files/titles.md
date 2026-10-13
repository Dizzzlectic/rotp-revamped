# Character titles

## Purpose

Supplies the character title names displayed by the client. This table contains
names; achievement requirements and rewards remain unchanged.

## Files

| Source                                                                 | Destination                                              | Text supplied         |
| ---------------------------------------------------------------------- | -------------------------------------------------------- | --------------------- |
| `data/luafiles514/lua files/datainfo/titletable.lub` in `kRO/data.grf` | `src/data/luafiles514/lua files/datainfo/titletable.lub` | Character title names |

See [inventory.json](../../inventory.json) for coverage and
[sources.json](../../sources.json) for reviewed sources and file-specific source
notes.

## Translation decisions

Title 1019, 목메여요, becomes “Choked Up,” using the emotional meaning of 목메다
described in the
[National Institute of Korean Language dictionary](https://krdict.korean.go.kr/eng/dicSearch/SearchView?ParaWordNo=55865).

## File format and client behavior

The replacement contains editable Lua source. `title_tbl` maps title IDs to
names, and `GetTitleString` returns a name or an empty string for an unknown ID.
Title IDs, `VIP` and the empty entries at IDs 1041 and 1042 are preserved.

The file contains ASCII text without a BOM and uses CRLF line endings. Its bytes
are identical in UTF-8 and CP949, matching the Korean client encoding.
