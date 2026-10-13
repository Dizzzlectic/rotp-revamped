# Ragnarok Online Translation Project — Revamped

**rotp-revamped** is an English translation project for Ragnarok Offline. It
aims to preserve the meaning, requirements and conditions of the game while
making its text clear and consistent. The initial scope is **Renewal**;
Pre-Renewal support is planned later.

## Translation references

In the development workspace, the
[translation project guide](../../docs/TRANSLATION_PROJECT.md) defines source
selection, review, unresolved decisions and documentation scope. Use
[terminology](docs/terminology.md) for shared names and gameplay terms, and the
[file documentation](docs/files/) for formats and specific translation
decisions.

## Project structure

```text
rotp-revamped/
├── README.md       project overview and development instructions
├── CHANGELOG.md    release history
├── LICENSE         GNU GPLv3 licence, also included in the package
├── inventory.json  translation targets and progress
├── sources.json    source versions and file hashes
├── docs/
│   ├── terminology.md  shared terms and names
│   └── files/          file purposes, paths, decisions and formats
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
        ├── cardpostfixnametable.txt  English suffix placement
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

Add translated files under `src/System/` and `src/data/` as needed. Item tables
must sit directly under `src/System/`, for example `src/System/itemInfo.lua`;
putting them under `src/System/LuaFiles514/` does not register them with the
client.

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

## Project records

- [inventory.json](inventory.json): targets, client support and translation
  coverage.
- [sources.json](sources.json): reviewed source versions, hashes and
  file-specific source notes.
- [review.csv](review.csv): pending wording decisions.
- [Changelog](CHANGELOG.md): release history.
- Development workspace
  [discrepancy tracker](../../docs/RATHENA_DISCREPANCIES.md): differences
  between client descriptions and server behavior.

## Development checks

Follow the
[independent review procedure](../../docs/TRANSLATION_PROJECT.md#independent-translation-review)
before considering a translation batch complete or packaging it.

Use kRO assets and **Your client's own text — Korean** with the mod enabled.
Untranslated client records remain Korean, making translation coverage visible.
Keep optional English art packs and unrelated translation mods off for this
check. Also check compatibility with **English translation** mode and the
navigation additions separately.

The app rebuilds assets when applying mod changes and requires the game client
to restart. Verify representative changes, preserved records, item artwork,
encoding and requirements. Disabling the mod should restore the base assets.
