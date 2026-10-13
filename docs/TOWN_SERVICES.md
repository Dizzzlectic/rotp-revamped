# Town and service labels

The source is `kRO/System/Towninfo.lub`. Its `mapNPCInfoTable` supplies labels
for service markers in the minimap and navigation interface.

The mod replaces it with editable Lua at `src/System/Towninfo.lub` and
`src/SystemEN/Towninfo.lub`. Both contain the same table because the client loads
`SystemEN` after `System` when that file exists. Map IDs, coordinates, service
types, entry order within each map and the `main()` registration behavior are
preserved.

## Wording

These labels describe places and services. Shop labels remain shops rather
than becoming dealer names. Generic services remain distinct from Kafra
services; “Rest Area” and “Guesthouse” retain their meanings rather than becoming
“Inn.” Named locations and guides retain their names.

The following Korean `name` values become the English `name` values in both
replacement files. iRO and ROenglishRE provide references where their wording
agrees with the source; their regional layouts and coordinates are not copied.

| Korean source | English              |
| ------------- | -------------------- |
| 편의서비스    | Convenience Services |
| 도구점        | Tool Shop            |
| 안내원        | Guide                |
| 무기점        | Weapon Shop          |
| 대장간        | Blacksmith's Shop    |
| 여관          | Inn                  |
| 스타일링샵    | Styling Salon        |
| 위치안내      | Directions           |
| 상점          | Shop                 |
| 방어구점      | Armor Shop           |
| 벨군드 연구실 | Belgund's Laboratory |
| 깃털 민박     | Feather Guesthouse   |
| 냐르의 창고   | Nyar's Warehouse     |
| 숙소          | Lodgings             |
| 카프라 서비스 | Kafra Services       |
| 쉼터          | Rest Area            |
| 창고          | Warehouse            |
| 상점과 창고   | Shop and Warehouse   |
| 상점 열매     | Fruit Shop           |
| 안내원 나비엘 | Naviel the Guide     |

## File format

The files contain UTF-8 Lua source without a BOM, with CRLF line endings.
Their English text uses only ASCII characters, whose bytes also match CP949
under the Korean client setting.
