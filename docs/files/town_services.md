# Town and service labels

## Purpose

Supplies town and service names for markers in the minimap and navigation
interface, such as shops, guides and storage. The translation changes labels
while preserving marker locations and service types.

## Files

| Source                    | Destination                 | Text supplied                             |
| ------------------------- | --------------------------- | ----------------------------------------- |
| `kRO/System/Towninfo.lub` | `src/System/Towninfo.lub`   | Town and service marker labels            |
| `kRO/System/Towninfo.lub` | `src/SystemEN/Towninfo.lub` | The same labels for the English text path |

See [inventory.json](../../inventory.json) for coverage and
[sources.json](../../sources.json) for reviewed sources and file-specific source
notes.

## Translation decisions

Shop labels remain shop names instead of naming dealers. Generic services stay
distinct from Kafra services. “Rest Area” and “Guesthouse” retain their meanings
instead of becoming “Inn.”

## File format and client behavior

`mapNPCInfoTable` supplies the marker labels. Both replacements contain the same
table because the client loads `SystemEN` after `System` when that file exists.
Map IDs, coordinates, service types, entry order within each map and the
`main()` registration behavior are preserved.

The files contain ASCII Lua source without a BOM and use CRLF line endings.
Their bytes are identical in UTF-8 and CP949, matching the Korean client
encoding.
