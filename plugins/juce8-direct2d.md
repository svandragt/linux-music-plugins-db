# JUCE 8 plugins needing Direct2D 1.3

*Status: confirmed broken · last checked 2026-08-10*

[Vendor page](https://juce.com/) · [All plugins](../README.md)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Black window and then a crash. JUCE 8 renders through Direct2D 1.3; Wine implements Direct2D to 1.2 and has no `dcomp.dll`. Affects any plugin built on JUCE 8 that does not ship a fallback renderer.

## Caveats and fixes

- Named in reports: Audio Modeling SWAM and Ambiente, Aberrant DSP, Hertz Drums, Synchro Arts VocAlign 6 Pro.
- Seen in Bitwig, REAPER and Mixbus — it is not host-specific.
- Two ways out, neither in yabridge's hands: the vendor ships a software-render fallback, or you run patched Wine.
- Counter-examples that do ship a fallback: Minimal Audio Squash, apulSoft apUnmask.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2024-12-18 | JUCE 8 plugins don't work — black screen and crash | Bitwig, REAPER, Mixbus | [#386](https://github.com/robbert-vdh/yabridge/issues/386) (closed 2026-06-04, reported by relaborn) |
| 2026-02-25 | BBC SO black screen, Superior Drummer 3 broken dropdowns | unspecified | [#467](https://github.com/robbert-vdh/yabridge/issues/467) (open, reported by sclewis900) |
| 2026-08-10 | Wine's Direct2D version gap | any host | [Wine bug 57833](https://list.winehq.org/hyperkitty/list/wine-bugs@list.winehq.org/message/VINNBRTJCXRSDT4IVS5HZODD753JMBXT/), [JUCE forum](https://forum.juce.com/t/juce8-direct2d-wine-yabridge/64298) |
