# Map names

## Source files and mod replacements

`kRO/` represents the Korean client folder.

| kRO source                                    | Mod destination             | Text supplied                                           |
| --------------------------------------------- | --------------------------- | ------------------------------------------------------- |
| `data/mapnametable.txt` inside `kRO/data.grf` | `src/data/mapnametable.txt` | General map labels                                      |
| `kRO/System/mapInfo_true.lub`                 | `src/System/mapInfo.lub`    | Display names and map-entry banner titles and subtitles |

The mod uses `mapInfo.lub` because the client checks that filename first. It
contains editable Lua source; the client accepts source as well as compiled Lua
under this filename. Both overrides translate complete tables while preserving
map identifiers, backgrounds and notification settings.

## Wording conventions

Repeated Korean labels use the same English wording in both tables.
Translations preserve regional names, directions, floor numbers and other
qualifiers. Numbered floors use `F1`, `F2`, etc.; explicitly numbered basement
levels use `B1`, `B2`, etc. “Upper Floors” and “Lower Floors” remain distinct.

ROenglishRE can help establish familiar English names, but its wording must
agree with the Korean source. Details it omits are retained, and newer entries
are translated directly from kRO.

## General labels: `mapnametable.txt`

Each entry has the form `map-resource#display-name#`. The following examples
show the Korean display name and its replacement in `src/data/mapnametable.txt`.

| Map resource   | Korean source                 | English                                        |
| -------------- | ----------------------------- | ---------------------------------------------- |
| `prontera.rsw` | 룬미드가츠 왕국 수도 프론테라 | Prontera, Capital of the Rune-Midgarts Kingdom |
| `izlude.rsw`   | 위성도시 이즈루드             | Satellite City of Izlude                       |
| `geffen.rsw`   | 마법도시 게펜                 | Magic City of Geffen                           |
| `payon.rsw`    | 산악도시 페이욘               | Mountain City of Payon                         |
| `morocc.rsw`   | 사막도시 모로크               | Desert City of Morroc                          |
| `alberta.rsw`  | 항구도시 알베르타             | Port City of Alberta                           |

## Entry banners: `mapInfo.lub`

`AddMapDisplayName(map, displayName, notifyEnter)` supplies the map-info display
name. `AddMapSignName(map, subTitle, mainTitle)` supplies the two banner lines.
These are separate fields and may contain different wording from the general
label in `mapnametable.txt`.

For the following towns, `mainTitle` is the translated city name shown in the
first column. The remaining columns show how the Korean `subTitle` in
`mapInfo_true.lub` becomes the English `subTitle` in `src/System/mapInfo.lub`:

| English `mainTitle` | Korean `subTitle`                  | English `subTitle`                                      |
| ------------------- | ---------------------------------- | ------------------------------------------------------- |
| Prontera            | 룬-미드가츠 왕국 수도              | Capital of the Rune-Midgarts Kingdom                    |
| Izlude              | 룬-미드가츠 왕국 프론테라 위성도시 | Satellite City of Prontera in the Rune-Midgarts Kingdom |
| Geffen              | 룬-미드가츠 왕국 마법도시          | Magic City of the Rune-Midgarts Kingdom                 |
| Payon               | 룬-미드가츠 왕국 산악도시          | Mountain City of the Rune-Midgarts Kingdom              |
| Morroc              | 룬-미드가츠 왕국 사막도시          | Desert City of the Rune-Midgarts Kingdom                |
| Alberta             | 룬-미드가츠 왕국 항구도시          | Port City of the Rune-Midgarts Kingdom                  |

## Encoding

Both files are stored as **UTF-8 without a BOM**, with CRLF line endings. They
contain only ASCII text, whose bytes are identical in UTF-8 and CP949, so they
remain compatible with the Korean client encoding.
