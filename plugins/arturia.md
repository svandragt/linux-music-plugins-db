[yabridge compatibility tracker](../README.md) › Arturia

# Arturia

*Status: verified · last checked 2026-08-10*

[Vendor page](https://www.arturia.com/)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Works with workarounds. Three separate reporters in 2026 alone, so the problems are well attested — as is the fact that people run them.

## Caveats and fixes

- Tooltip GUI freeze: enable 'Hide Wine version from applications' in winecfg's Staging tab.
- VST3 hitbox and mouse misalignment on Wayland + KDE; a virtual desktop works around it (#497).
- REAPER crash when changing track channels with the GUI open (#468) and FPS drops on track selection (#473).
- Memory errors at the end of a VST3 scan were fixed in yabridge.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2026-08-06 | VST3 GUI hitbox and mouse misalignment, solved via virtual desktop | Wayland + KDE | [#497](https://github.com/robbert-vdh/yabridge/issues/497) (open, reported by Leadsingerman0503) |
| 2026-02-25 | Crash when the plugin UI is open and track channels change | REAPER | [#468](https://github.com/robbert-vdh/yabridge/issues/468) (open, reported by duck-117) |
| 2026-04-08 | Large FPS drops when the plugin's track is selected | REAPER | [#473](https://github.com/robbert-vdh/yabridge/issues/473) (open, reported by illegitimate-egg) |
| 2026-08-10 | Tooltip freeze workaround; VST3 scan memory fix | any host | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes), [CHANGELOG](https://github.com/robbert-vdh/yabridge/blob/master/CHANGELOG.md) |

---

[Back to the tracker index](../README.md) · [How to correct this page](../CONTRIBUTING.md)
