# Achievement text

`src/System/achievement_list.lub` replaces the kRO achievement table. Its 361
records contain titles, summaries, descriptions and objective labels. The client
loads `achievement_tbl` when achievements are enabled.

## Wording

kRO supplies the meaning. iRO and ROenglishRE provide reference wording, checked
by achievement ID. Humor remains in the titles; requirements use direct English
such as “Reach Base Level 100” and “Successfully refine a level 2 weapon to +7.”
Place names match the map translations, and linked objectives use the matching
achievement titles. [Terminology](TERMINOLOGY.md) defines shared gameplay terms.

The [official iRO overview](https://iro.ragnarokonline.com/news/updatedetail.aspx?id=291),
[kRO developer note](https://ro.gnjoy.com/news/devnote/View.asp?category=3&curpage=6&seq=1669396),
and [iRO achievement list](https://irowiki.org/wiki/Achievement_System) provide
system context and wording references. Regional descriptions are not treated as
proof of matching requirements. Source versions and hashes are in
[sources.json](../sources.json).

## Pending review

Conflicting or unimplemented requirements in 26 achievements remain Korean. Proposed English and exact
field paths are in [review.csv](../review.csv). In the development workspace,
the root `docs/RATHENA_DISCREPANCIES.md` lists the implementation differences.
Unaffected fields are translated.

Two non-text source issues are preserved: achievement 200024 uses reward buff
icon 611 while rAthena grants icon 305, and 129019 links to nonexistent shortcut
120918 instead of 129018. Neither changes the meaning of the translated text.

## File format

The source is compiled Lua 5.1. The replacement is readable Lua source, encoded
as CP949 without a BOM, with CRLF line endings. English text is ASCII; CP949
preserves the fields held in Korean. Numeric IDs, counts, scores, rewards,
shortcuts, category keys and display settings remain unchanged. The `main()`
registration helper retains the source's callbacks and error handling.
