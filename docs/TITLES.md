# Character titles

The source is `data/luafiles514/lua files/datainfo/titletable.lub` inside
`kRO/data.grf`. The mod replaces it at
`src/data/luafiles514/lua files/datainfo/titletable.lub`.

The replacement contains editable Lua source. `title_tbl` maps title IDs to
names, and `GetTitleString` returns a name or an empty string for an unknown ID.
Title IDs, `VIP` and the empty entries at IDs 1041 and 1042 are preserved.
Achievement requirements and rewards remain unchanged.

## Wording

Titles retain their Korean meaning, including metaphors and descriptive
phrases. English reference tables can differ in wording and assign different
names to the same ID; matching an ID alone does not establish agreement.

| Title ID | Korean source       | English                 |
| -------- | ------------------- | ----------------------- |
| 1010     | 금강불괴의          | Indestructible          |
| 1013     | 천운의              | Heavenly Fortune        |
| 1017     | 피의 색깔은 빨간색  | Blood Is Red            |
| 1019     | 목메여요            | Choked Up               |
| 1024     | 파워 노력가         | Super Hard Worker       |
| 1031     | 남이 못보는 걸 보는 | Sees What Others Cannot |
| 1035     | 데스 슬레이어       | Death Slayer            |
| 1036     | 언데드 슬레이어     | Undead Slayer           |

“Choked Up” uses the emotional meaning of 목메다, described in the
[National Institute of Korean Language dictionary](https://krdict.korean.go.kr/eng/dicSearch/SearchView?ParaWordNo=55865).

## File format

The file is stored as UTF-8 without a BOM, with CRLF line endings. Its English
text uses only ASCII characters, whose bytes also match CP949 as expected by
the Korean client setting.
