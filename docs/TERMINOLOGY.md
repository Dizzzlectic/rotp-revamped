# Translation terminology

Use the same wording for the same concept across translated files. Match named
UI labels when referring to them directly. Ordinary prose may use sentence
casing and deliberate expanded wording where it reads naturally; consistency
does not require mechanically capitalizing every occurrence. Correct spelling
mistakes in source English rather than carrying them into the translation.

Preserve intentional dialogue voices, jokes and proper names. These exceptions
do not justify inconsistent gameplay terminology. Source identifiers remain
unchanged. Add recurring terms here as translation coverage grows, and check
new wording against the existing suite during independent review.

## Stat labels and explanations

Stat labels, numeric bonuses and messages referring to named stats use the
labels below. Explanatory tooltips use their full names. Abbreviations retain
their capitalization and punctuation in every translated file; Critical is
written out for the critical-chance stat.

| Stat label      | Explanatory name        |
| --------------- | ----------------------- |
| STR             | Strength                |
| AGI             | Agility                 |
| VIT             | Vitality                |
| INT             | Intelligence            |
| DEX             | Dexterity               |
| LUK             | Luck                    |
| HP / SP         | HP / SP                 |
| Max HP / Max SP | Maximum HP / Maximum SP |
| ATK             | Physical attack         |
| MATK            | Magic attack            |
| DEF             | Physical defense        |
| MDEF            | Magic defense           |
| HIT             | Accuracy                |
| FLEE            | Evasion                 |
| Critical        | Critical hit chance     |
| ASPD            | Attack speed            |
| POW             | Power                   |
| SPL             | Spell                   |
| STA             | Stamina                 |
| WIS             | Wisdom                  |
| CON             | Concentration           |
| CRT             | Creativity              |
| P.ATK           | Trait physical attack   |
| S.MATK          | Trait magic attack      |
| RES             | Physical resistance     |
| MRES            | Magic resistance        |
| H.PLUS          | Trait healing amount    |
| C.RATE          | Critical damage rate    |

## Distinct effects

- **Critical** describes critical hit chance when used as a stat label or
  numeric bonus. **Critical damage** describes damage dealt by critical hits;
  **non-critical physical damage** describes eligible physical hits that do not
  crit. `CRI` and `Crit` are not alternate translated stat labels.
- **C.RATE** is a separate trait stat. It is not critical hit chance or the ordinary critical
  damage bonus.
- **Perfect Dodge** and **Perfect Hit chance** are separate effects from FLEE
  and HIT.

Source identifiers and proper names retain their spelling. A card affix named
“Critical,” for example, is a name rather than a stat label.
Reference quotations and Korean records awaiting review remain unchanged.

Consistent terminology does not change numeric units or scaling. Whether an
option value needs division by ten is a separate question from calling its
stat Critical.

CRT uses **Creativity**, the natural English noun for kRO’s “Creative” label.
[The kRO status guide](https://ro.gnjoy.com/guide/ragstart/basic2.asp) uses the
Creative loanword; [iRO’s CRT item explanation](https://iro.ragnarokonline.com/news/eventdetail.aspx?id=1608&p=4)
also uses “creativity.” The stat affects trait healing amount and critical
damage rate.

## Gameplay terms

| Concept | Wording |
| --- | --- |
| Character and job progression | Base Level, Job Level, Base EXP, Job EXP |
| Achievement progression | Achievement Level; distinct from Base Level |
| Unmodified stat requirement | base STR, base INT, and equivalent stat labels |
| Currency | Zeny |
| Refine levels | refine; refining; refinement; +7 for the resulting refine level |
| Equipment grades | grade; grading; grade enhancement; Grade D through Grade A |
| Equipment enchants | enchant; enchanting; enchantment; an added or changed enchant effect |
| Monster objective | defeat; reserve taming for making a monster a pet |
| Achievement dependency | Complete "Achievement Title" |

Use Base EXP and Job EXP for rewards, bonuses and interface text. Spelling out
“experience” is acceptable when deliberate prose makes the relevant type clear.
Base Level and Job Level are named labels; “base level” and “job level” are
appropriate in ordinary sentences or incantations. Achievement Level refers
to achievement progression, not character progression or an equipment grade.

Refining changes the equipment's + level. Grading changes its letter grade.
Enchanting adds or changes enchant effects. Avoid the generic “enhancing” when
the specific action is known. These systems remain distinct even where a
source uses “Grade Enchanter” as an NPC name. See Gravity's
[grade guide](https://ro.gnjoy.in.th/item-gradereform/) and
[iRO enchantment example](https://iro.ragnarokonline.com/news/updatedetail.aspx?id=383).

## Names and casing

| Concept | Preferred wording | Context |
| --- | --- | --- |
| Place name | Rune-Midgarts | Not Rune-Midgard |
| City and monster | Morroc; Morocc | Morroc is the city; Morocc is the monster. Do not merge these names. |
| Port destination | Rockridge | Use the same spelling on maps and signboards. |
| Numbered floors | F1, F2; B1, B2 | Use B only where the source establishes a basement floor. |
| Job names | Title case | Archbishop and Whitesmith are single words. |
| Elements and races | Title case | Shadow and Demi-Human name specific game categories. |
| Pet states | Match the UI labels below | Explanatory dialogue uses the same state names. |
| Stat explanations | Sentence case in prose | “Physical attack” is a tooltip caption; “physical attack” fits within a sentence. |

Place names follow the map translations. Item and monster names retain
established spellings when they agree with kRO and the supported implementation.
Card affixes and achievement titles are proper names; a word such as Critical
or Wisdom in one of those names does not necessarily describe a stat.

## Job names

These are established project spellings, not alternate names inferred from
source identifiers. Keep job variants and progression stages distinct. Regional
aliases require source comparison before replacing an established name.

| Group | Names |
| --- | --- |
| Novice and first jobs | Novice, Swordman, Magician, Archer, Acolyte, Merchant, Thief |
| Reborn novice and first jobs | High Novice, High Swordman, High Magician, High Archer, High Acolyte, High Merchant, High Thief |
| Second jobs | Knight, Priest, Wizard, Blacksmith, Hunter, Assassin, Crusader, Monk, Sage, Rogue, Alchemist, Bard, Dancer |
| Transcendent second jobs | Lord Knight, High Priest, High Wizard, Whitesmith, Sniper, Assassin Cross, Paladin, Champion, Professor, Stalker, Creator, Clown, Gypsy |
| Third jobs | Rune Knight, Archbishop, Warlock, Mechanic, Ranger, Guillotine Cross, Royal Guard, Sura, Sorcerer, Shadow Chaser, Genetic, Minstrel, Wanderer |
| Other jobs | Super Novice, Gunslinger, Rebellion, Ninja, Kagerou, Oboro, Taekwon Boy, Taekwon Girl, Star Gladiator, Star Emperor, Soul Linker, Soul Reaper, Summoner |
| Fourth jobs named in the message table | Imperial Guard, Abyss Chaser, Windhawk |

## Elements and races

| Category | Names |
| --- | --- |
| Elements | Neutral, Water, Earth, Fire, Wind, Poison, Holy, Shadow, Ghost, Undead |
| Monster races | Formless, Undead, Brute, Plant, Insect, Fish, Demon, Demi-Human, Angel, Dragon |
| Player categories | Human players, Doram players |

Use Shadow for the element rather than Dark. Use Brute, Fish, Demon and
Demi-Human for the corresponding monster races rather than Animal, Marine,
Devil and Human. Human players are a separate category from Demi-Human
monsters. Undead can describe an element or a race; preserve the source's
distinction in effect descriptions.

## Pet states

States are listed from lowest to highest. Hunger and intimacy are separate
systems; their shared Normal label does not make them interchangeable.

| System | UI labels |
| --- | --- |
| Hunger | Hungry, Peckish, Normal, Full, Very Full |
| Intimacy | Distant, Awkward, Normal, Friendly, Loyal |

When naming a state in dialogue, use the UI wording: “when its hunger status is
Normal” or “its intimacy must be Loyal.” Ordinary descriptions such as “I'm
hungry” remain natural dialogue and do not require capitalization.
