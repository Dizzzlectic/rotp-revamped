# Map signboard text

## Purpose

Supplies text displayed on map signboards, including service names, travel
destinations and entry restrictions. Records without text descriptions refer to
images; lettering inside those images requires separate artwork translation.

## Files

| Source                                                           | Destination                                        | Text supplied              |
| ---------------------------------------------------------------- | -------------------------------------------------- | -------------------------- |
| `data/luafiles514/lua files/SignBoardList.lub` in `kRO/data.grf` | `src/data/luafiles514/lua files/SignBoardList.lub` | Map signboard descriptions |

See [inventory.json](../../inventory.json) for coverage and
[sources.json](../../sources.json) for reviewed sources and file-specific source
notes.

## Translation decisions

Level restrictions retain inclusive lower bounds: `180Lv미만 출입금지` becomes
“Entry: Level 180+.” Airship routes retain both named destinations, such as
“유노-라헬 행” becoming “To Yuno and Rachel.”

“입력안하셨습니다” becomes “No text entered,” describing missing input rather
than ROenglishRE's “Cannot enter.” “Biosphere” and “Specimen Environment” remain
distinct where kRO uses different labels.

## File format and client behavior

Only the seventh field, the text description, changes. Leading spaces are
preserved. Map IDs, coordinates, height, display type, resource paths and colors
are preserved. The client loads the mod table after the base and merges records
by map and cell.

The replacement is editable Lua source stored as UTF-8 without a BOM, with CRLF
line endings. English text uses ASCII bytes. Korean resource names use Lua
decimal byte escapes to preserve their original CP949 bytes while keeping the
source file readable as UTF-8.
