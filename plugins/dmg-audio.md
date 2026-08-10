[yabridge compatibility tracker](../README.md) › DMG Audio

# DMG Audio

*Status: reported, mixed · last checked 2026-08-10*

[Vendor page](https://dmgaudio.com/)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Host-dependent. Typing a precise value into Limitless or TrackControl works in
REAPER and stops after the first keypress in Bitwig Studio; the mouse still works
in both. A separate reporter names DMG Audio alongside Pulsar Audio in a freeze
report, without detail. An older freeze in REAPER, when the plugin resized itself,
was fixed in yabridge itself.

## Caveats and fixes

- Bitwig workaround from the reporter who confirmed the bug: nudge the value with
  the mouse, then type the number into Bitwig's own device control instead of the
  plugin's field.
- Affects both VST2 and VST3.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2024-09-06 | Keyboard value entry in Limitless and TrackControl registers only the first keypress; works as expected in REAPER | Gentoo, Bitwig Studio, yabridge 5.1, VST2 and VST3 | [#367](https://github.com/robbert-vdh/yabridge/issues/367) (open, reported by kuchtamartin) |
| 2024-10-04 | Confirmed in the VST3 versions of Limitless and Track Control, with a Bitwig workaround | Bitwig Studio | [#367](https://github.com/robbert-vdh/yabridge/issues/367) (relaborn) |
| 2025-08-01 | Named alongside Pulsar Audio in a host-freeze report; no further detail | Fedora KDE 42, REAPER and Renoise, Wine 9.21 | [#426](https://github.com/robbert-vdh/yabridge/issues/426) (untilde) |
| 2021-06-03 | DMG VST3 plugins freezing in REAPER on self-resize, and when restoring several instances at once, fixed in yabridge 3.3.0 | REAPER | [yabridge CHANGELOG](https://github.com/robbert-vdh/yabridge/blob/master/CHANGELOG.md) |

---

[Back to the tracker index](../README.md) · [How to correct this page](../CONTRIBUTING.md)
