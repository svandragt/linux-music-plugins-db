[yabridge compatibility tracker](../README.md) › Pulsar Audio

# Pulsar Audio

*Status: reported · last checked 2026-08-10*

[Vendor page](https://pulsar.audio/poseidon/)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Reported to hang the host rather than fail cleanly. Poseidon stalls Renoise
indefinitely when a saved song containing it is loaded, with no 'plugin failed'
message to point at the culprit — the reporter found it by elimination. A second
person in the same thread reports the same freeze with other Pulsar plugins, worse
in REAPER than in Renoise. One thread, so this stays single-sourced.

## Caveats and fixes

- No fix known. If a project hangs on load, move the yabridge `.vst3` directory
  aside and reintroduce plugin folders one at a time; that is how the reporter
  recovered the project.
- iLok was suggested as the cause and then ruled out by the second reporter, who
  states Pulsar does not use iLok.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2025-05-06 | Poseidon hangs Renoise indefinitely on song load; needs `killall`, no error message | Renoise | [#426](https://github.com/robbert-vdh/yabridge/issues/426) (open, reported by 0CCULTIST) |
| 2025-08-01 | Same freeze with other Pulsar plugins, more often in REAPER than Renoise; states Pulsar does not use iLok | Fedora KDE 42, Wine 9.21, latest yabridge, DXVK | [#426](https://github.com/robbert-vdh/yabridge/issues/426) (untilde, same thread) |

---

[Back to the tracker index](../README.md) · [How to correct this page](../CONTRIBUTING.md)
