# Ragnarok Online Translation Project — Revamped

**rotp-revamped** is an English translation project for Ragnarok Offline.
It aims to preserve the meaning, requirements and conditions of the game while
making its text clear and consistent. The initial scope is **Renewal**;
Pre-Renewal support is planned later.

## Translation policy

- The app's pinned rAthena fork, selected era and active gameplay modifications
  define supported game behavior.
- kRO wording and data provide evidence of official meaning and intent.
- iRO and ROenglishRE provide structure and wording inspiration. Copy wording
  only after establishing substantial agreement with kRO.
- When rAthena and kRO disagree about an item or monster, record its ID and the
  conflicting evidence for manual review. Leave it out of the new translation
  until that review is complete.

Use the [terminology reference](docs/TERMINOLOGY.md) for shared names, gameplay
terms, stat explanations and casing.

Start with small files and selected records, then expand to more complex items,
quests and other game text. Keep research evidence and review records outside
the distributed mod.

## Project structure

```text
rotp-revamped/
├── README.md       project overview and development instructions
├── CHANGELOG.md    release history
├── LICENSE         GNU GPLv3 licence, also included in the package
├── inventory.json  translation targets and progress
├── sources.json    source versions and file hashes
├── docs/           translation sources and file formats
├── scripts/
│   └── package.py  builds the distributable ZIP
└── src/            source of the distributed mod
    ├── mod.json    mod identity and compatibility requirements
    ├── README.md   introduction shown in the app
    ├── System/
    │   ├── achievement_list.lub  achievement text
    │   ├── mapInfo.lub       map-entry titles and display settings
    │   └── Towninfo.lub      town and service labels
    ├── SystemEN/
    │   └── Towninfo.lub      town and service labels in English text mode
    └── data/
        ├── cardprefixnametable.txt  card prefixes and suffixes
        ├── mapnametable.txt  map display names
        ├── msgstringtable.csv  client interface messages and errors
        ├── ba_frostjoke.txt    Frost Joke dialogue
        ├── dc_scream.txt       Scream dialogue
        ├── pettalktable.xml    pet dialogue
        └── luafiles514/lua files/
            ├── SignBoardList.lub  map signboard text
            └── datainfo/
                ├── addrandomoptionnametable.lub  equipment random options
                └── titletable.lub  character title names
```

Add translated files under `src/System/` and `src/data/` as needed. These folders
are not required while empty. Item tables must sit directly under
`src/System/`, for example `src/System/itemInfo.lua`; putting them under
`src/System/LuaFiles514/` does not register them with the client.

## Packaging and installation

From the project folder, run:

```sh
python3 scripts/package.py
```

The script uses only Python's standard library. It reads the name and version
from `src/mod.json`, stages the contents of `src/` and the project LICENSE under
`rotp-revamped/`, and writes `dist/<name>-<version>.zip`. Staging is temporary;
rerunning replaces the archive for that version.

Import the ZIP through **Settings → Mods**. The archive contains
`rotp-revamped/mod.json` directly, with the app README and any translated files
beside it. Use the archive for local checks too: importing `src/` as a folder
would install the mod under the wrong name.

## Translation inventory

[inventory.json](inventory.json) lists translation targets, source and mod
paths, client support, status and completed/total record counts. Unknown totals
remain `null`. The catalog is still being expanded and does not yet cover every
client text file, translated image or server script. Source hashes and patch
metadata remain in `sources.json`. When records need manual review, create
`review.csv` to record them by stable ID and retain their source text where a
whole-file replacement is required. Remove the queue when all entries are
resolved.

In the Ragnarok Offline development workspace, the root
`docs/RATHENA_DISCREPANCIES.md` tracks open differences between kRO descriptions
and server behavior. Record source text, code locations and issue or PR links;
approving wording alone does not resolve a server discrepancy.

## Source updates

[sources.json](sources.json) records client patch IDs, UTC file modification
times and SHA-256 hashes for reviewed sources and their translations. After
updating a client, compare the relevant source hashes to identify completed
translations that need review. For a file inside a GRF, compare the extracted
file's hash; the archive timestamp alone does not show whether that file changed.
Update a source hash after reviewing the changed source and its translation.

## Development checks

Each translation batch, including batches revising existing translations,
requires a fresh, dedicated reviewer subagent that did not write it. Before packaging or marking the work
complete, have it review every changed string against the source and the entire
translated suite for accuracy, consistent wording, terminology and casing,
spelling, and natural English. The reviewer reports actionable findings in chat
without editing; resolve confirmed findings and have it check corrections.
Report limitations explicitly and keep pending decisions in `review.csv`,
without historical review logs. Update the inventory and source records when
the batch is finished.

Use kRO assets and **Your client's own text — Korean** with the mod
enabled. Untranslated client records remain Korean, making translation coverage
visible. Keep optional English art packs and unrelated translation mods off for
this check. Also check compatibility with **English translation** mode and the
navigation additions separately.

The app rebuilds assets when applying mod changes and requires the game client
to restart. Verify representative changes, preserved records, item artwork,
encoding and requirements. Disabling the mod should restore the base assets.
