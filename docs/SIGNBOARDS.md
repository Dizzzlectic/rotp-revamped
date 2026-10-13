# Map signboard text

The source is `data/luafiles514/lua files/SignBoardList.lub` inside
`kRO/data.grf`. The mod provides its replacement at
`src/data/luafiles514/lua files/SignBoardList.lub`.

`SignBoardList` contains 925 records across 133 maps. All 139 populated
descriptions are translated, covering 71 distinct labels. The remaining records
refer to images without a text description; lettering inside those images
requires separate artwork translation.

Each record retains its map ID, coordinates, height, display type, resource
path and color. Only the seventh field, the text description, changes. The
client loads the mod table after the base and merges records by map and cell.

## Wording

iRO descriptions at matching map coordinates and ROenglishRE's
`SystemEN/Sign_Data.lub` provide wording references where they agree with kRO.
Their layouts and translation helpers are not copied. Destination names follow
the mod's map tables, including Yuno, Kunlun, Louyang and Jawaii.

The following Korean descriptions become the English descriptions in the
replacement. Leading spaces are retained but omitted from these examples.

| Korean source      | English                             |
| ------------------ | ----------------------------------- |
| 입력안하셨습니다   | No text entered                     |
| 모험가 편의센터    | Adventurer Service Center           |
| 180Lv미만 출입금지 | Entry: Level 180+                   |
| 190Lv미만 출입금지 | Entry: Level 190+                   |
| 표본 환경 - 혹한   | Specimen Environment - Extreme Cold |
| 낙원단 공간이동사  | Eden Group Teleporter               |
| 1차 전직 안내      | First Job Change Guide              |
| 여객선 승선        | Ferry Boarding                      |
| 용지성 행          | To Louyang                          |
| 거북섬 행          | To Turtle Island                    |
| 비공정 출구        | Airship Exit                        |
| 유노-라헬 행       | To Yuno and Rachel                  |
| 슈발츠발드 국내선  | Schwarzwald Domestic Flights        |
| 등급강화소         | Grade Enhancement Workshop          |

Level restrictions retain the inclusive lower bounds. Airship route labels
retain both named destinations. “No text entered” describes missing input;
ROenglishRE's “Cannot enter” changes that meaning. “Biosphere” and
“Specimen Environment” remain distinct where kRO uses different labels.

## File format

The replacement is editable Lua source stored as UTF-8 without a BOM, with
CRLF line endings. Its English text uses only ASCII characters, which also
decode correctly under the Korean client setting. Korean resource names are
represented with Lua decimal byte escapes to preserve their original CP949
bytes without leaving non-UTF-8 text in the source file.
