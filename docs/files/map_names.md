# Map names

## Purpose

Supplies map display names and the titles and subtitles shown in map-entry
banners. General map labels and banner text are separate fields and may use
different wording for the same location.

## Files

| Source                                    | Destination                 | Text supplied                                |
| ----------------------------------------- | --------------------------- | -------------------------------------------- |
| `data/mapnametable.txt` in `kRO/data.grf` | `src/data/mapnametable.txt` | General map labels                           |
| `kRO/System/mapInfo_true.lub`             | `src/System/mapInfo.lub`    | Map-info display names and entry-banner text |

See [inventory.json](../../inventory.json) for coverage and
[sources.json](../../sources.json) for reviewed sources and file-specific source
notes.

## Translation decisions

Retain town descriptors omitted by ROenglishRE, such as Prontera's role as the
capital and Izlude's role as a satellite city. Keep “Upper Floors” and “Lower
Floors” as distinct labels instead of assigning unsupported floor numbers.

`prtg_cas03` and its siege-simulation maps use **Fadhgridh**, the established
iRO and ROenglishRE name for kRO's 라즈리그스. The castle banner uses “Valkyrie
Realm” as its subtitle and “Fadhgridh” as its main title.

## File format and client behavior

The client checks `mapInfo.lub` before `mapInfo_true.lub` and accepts readable
Lua source as well as compiled Lua under this filename. Both overrides preserve
map identifiers, backgrounds and notification settings.

`mapnametable.txt` records have the form `map-resource#display-name#`. In
`mapInfo.lub`, `AddMapDisplayName(map, displayName, notifyEnter)` supplies the
map-info display name, while `AddMapSignName(map, subTitle, mainTitle)` supplies
the two banner lines. These are separate fields and can use different wording.

For example, Prontera's general label is “Prontera, Capital of the Rune-Midgarts
Kingdom.” Its banner splits this into `mainTitle` “Prontera” and `subTitle`
“Capital of the Rune-Midgarts Kingdom.”

Both files contain ASCII text without a BOM and use CRLF line endings. Their
bytes are identical in UTF-8 and CP949, matching the Korean client encoding.
