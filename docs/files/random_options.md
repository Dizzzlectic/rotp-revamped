# Equipment random options

## Purpose

Supplies the random-option descriptions shown in item details and equipment
comparisons. The text explains bonuses and numeric values; it does not change
the bonuses applied by the server.

## Files

| Source                                                                               | Destination                                                            | Text supplied                    |
| ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- | -------------------------------- |
| `data/luafiles514/lua files/datainfo/addrandomoptionnametable.lub` in `kRO/data.grf` | `src/data/luafiles514/lua files/datainfo/addrandomoptionnametable.lub` | Random-option bonus descriptions |

See [inventory.json](../../inventory.json) for coverage and
[sources.json](../../sources.json) for reviewed sources and file-specific source
notes.

## Translation decisions

Options 149–150 and 160–162 explicitly describe **physical damage** from the
specified enemy class or size. Options 204–205 use “Ranged weapon damage” and
“Ranged weapon damage taken,” meaning physical weapon attacks. These names do
not establish equivalence with the general ranged bonuses in options 166–167.
The reviewed rAthena source has no corresponding definitions for 204–205.

Options 255–256 use “Non-critical physical damage” and “Non-critical physical
damage taken.”
[Gravity's explanation](https://ro.gnjoy.com/news/devnote/View.asp?category=1&curpage=1&seq=4194130)
excludes certain special damage formulas from the outgoing bonus. iRO's ID 255
is its `END` marker, so matching that ID is not a wording reference. The
defensive option's exact formula and exclusions remain unverified. The reviewed
rAthena source has no definitions for these options and no matching non-critical
damage reduction bonus.

Options 117–126 use iRO's division expression, such as
`Critical + (%d / 10) against Formless monsters`. rAthena divides the stored
value by ten using integer division. The client substitutes `%d` without
evaluating arithmetic: a stored value of 10 displays as `Critical + (10 / 10)`,
while rAthena applies +1. Values not divisible by ten truncate on the server.

Race resistance options 194–203 retain general resistance wording: rAthena's
`cardfix_monster_physical` setting makes their reductions apply to monster magic
as well as weapon attacks.

## File format and client behavior

The replacement is Lua source despite the `.lub` extension. `NameTable_VAR` uses
IDs supplied by the unchanged `enumvar.lub`; keys and the `END` sentinel are
preserved. The client substitutes the option value into `%d` and renders `%%` as
`%`. These markers remain unchanged for every entry.

The file contains ASCII text without a BOM and uses CRLF line endings. Its bytes
are identical in CP949 and UTF-8, so both client text modes can read it.
