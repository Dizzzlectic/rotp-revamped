# Equipment random options

The source is `data/luafiles514/lua files/datainfo/addrandomoptionnametable.lub`
inside `kRO/data.grf`. The mod replaces the same path under `src/`. These
descriptions appear in item details and equipment comparisons; they do not
change the bonuses applied by the server.

All 253 bonus descriptions are translated; the `END` sentinel is unchanged.
Options 149–150 and 160–162 use the approved physical-damage wording from kRO.
Their server fixes remain separate from translation approval.

The development workspace's root `docs/RATHENA_DISCREPANCIES.md` records their
Korean text, approved English, effects and implementing code.

Options 204–205 are translated as “Ranged weapon damage” and “Ranged weapon
damage taken,” following the agreement between kRO and iRO. Here, weapon
damage means physical weapon attacks. Their rAthena definitions are still
missing; the approved labels do not establish server support or equivalence
with the general ranged bonuses in options 166–167.

Options 255–256 use “Non-critical physical damage” and “Non-critical physical
damage taken.” This refers to eligible physical attacks that do not crit,
including skills. [Gravity’s explanation](https://ro.gnjoy.com/news/devnote/View.asp?category=1&curpage=1&seq=4194130)
excludes certain special damage formulas from the outgoing bonus. iRO has no
matching descriptions; its ID 255 is the `END` marker. rAthena has an outgoing
`bNonCritAtkRate` bonus but neither random-option definition nor a matching
non-critical damage reduction bonus. The defensive option’s exact formula
and exclusions remain unverified.

Options 117–126 use iRO’s division expression with the Critical label, such as
`Critical + (%d / 10) against Formless monsters`. rAthena divides the stored
value by ten using integer division. The client substitutes `%d` without
evaluating arithmetic: a stored value of 10 displays as `Critical + (10 / 10)`,
while rAthena applies +1. Values not divisible by ten truncate on the server.
The full labels also include the affected monster race.

## Wording

kRO supplies the meaning; the Renewal rAthena option scripts, bonus handling
and battle configuration establish the supported behavior. iRO and ROenglishRE
provide reference terminology where it agrees with that evidence.

Attack elements and enemy elements are distinct: “Fire magic damage” describes
the attack, while “Magic damage to Fire element enemies” describes its target.
Undead element enemies are likewise distinct from Undead race monsters.
Demihuman monsters, Human players and Doram players remain separate categories.

The following source descriptions become the English descriptions shown here:

| Option ID | Korean source                          | English                                     |
| --------- | -------------------------------------- | ------------------------------------------- |
| 11        | HP 자연회복 속도 %d%% 증가             | Natural HP recovery +%d%%                   |
| 16        | 공격속도 증가(공격 후딜레이 %d%% 감소) | Attack speed increased (attack delay -%d%%) |
| 63        | 화속성 적에게 마법 데미지 %d%% 증가    | Magic damage to Fire element enemies +%d%%  |
| 169       | 받는 힐량 %d%% 증가                    | Healing received +%d%%                      |
| 171       | 글로벌 쿨타임 %d%% 감소                | After-cast delay -%d%%                      |
| 224       | 화속성 마법 데미지 %d%% 증가           | Fire magic damage +%d%%                     |

Natural recovery bonuses increase the amount recovered rather than shortening
the interval. After-cast delay is the shared delay after a skill, rather than
that skill's individual cooldown. Race resistance options 194–203 retain
general resistance wording: rAthena's `cardfix_monster_physical` setting makes
their reductions apply to monster magic as well as weapon attacks.

## File format

The replacement is Lua source despite the `.lub` extension. `NameTable_VAR`
uses IDs supplied by the unchanged `enumvar.lub`; all 254 keys and the `END`
sentinel are preserved. The client substitutes the option value into `%d` and
renders `%%` as `%`. These markers remain unchanged for every entry.

The file contains only ASCII text, without a BOM, and uses CRLF line endings.
Its bytes are identical in CP949 and UTF-8, so both client text modes can read
the same file.
