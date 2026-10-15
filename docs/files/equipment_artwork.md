# Equipment background labels

## Purpose

Supplies the faint slot labels behind items in the General equipment tab.
The labels are part of the background image, rather than client messages.

## Files

| Source                                                                          | Destination                                           | Text supplied                              |
| ------------------------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------ |
| `data/texture/유저인터페이스/basic_interface/equipwin_bg.bmp` in `kRO/data.grf` | `src/data/texture/ui/basic_interface/equipwin_bg.bmp` | General equipment slot labels              |
| The same path in `iRO/data.grf`                                                 | Reference artwork                                     | Correct accessory spelling and R/L markers |

See [inventory.json](../../inventory.json) for coverage and
[sources.json](../../sources.json) for source versions and hashes.

## Translation decisions

The kRO labels are already English, but both accessory captions spell the word
as “accessary.” Reuse iRO's corrected lettering and R/L markers for those two
slots. Keep the other captions, including the three generic “head” labels.

## File format and client behavior

The replacement retains kRO's 280 × 130 dimensions, indexed 8-bit BMP format,
palette and borders. iRO's reference is a 280 × 150 RGB bitmap; only its label
regions are transferred, without scaling its letters or adding its bottom strip.
Colors are mapped to the existing palette, differing by at most one per RGB
channel. The client displays this background in a 280 × 130 equipment table.

The mod uses the app's ASCII `data/texture/ui/` alias. During asset staging, the
app expands it to the client's CP949 directory spelling. Keeping the archive
path ASCII avoids platform-dependent filename decoding during installation;
see the [modding guide](../../../../ragnarokoffline.app/docs/MODDING.md#you-can-write-ascii-instead-of-mojibake).
