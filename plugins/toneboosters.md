[yabridge compatibility tracker](../README.md) › ToneBoosters

# ToneBoosters

*Status: confirmed broken · last checked 2026-08-10*

[Vendor page](https://www.toneboosters.com/)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Bridged ToneBoosters plugins show a black window instead of their interface. The
vendor answered the report directly: their plugins need Direct2D feature set 1.3,
Wine implements up to 1.2. That is the same wall as the
[JUCE 8 / Direct2D 1.3](juce8-direct2d.md) entry, and the plugin binaries were
confirmed to be JUCE 8.

There is no reason to bridge these at all now — ToneBoosters ship a Linux build.

## Native alternative

ToneBoosters publish a Linux plugin archive. The vendor's download section lists
**Plugin archive v2.1.8 (July 2026) for Linux; requires a 64-bit DAW with VST or
VST3 support; Intel or AMD SSE2 processor; glibc version 2.31 or up**, next to the
Windows and macOS installers. Checked 2026-08-10 on
[toneboosters.com](https://www.toneboosters.com/).

## Caveats and fixes

- No workaround for the bridged version. DXVK does not fix a missing Direct2D
  feature level.
- A JUCE 7 build of a plugin, if the vendor still has one, does work — that is the
  general escape route for this class of failure, not something ToneBoosters offer.
- Check what you actually have with `strings <plugin>.vst3 | grep 'JUCE v'`.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2025-04-17 | All ToneBoosters plugins show a black screen instead of the GUI | Linux Mint 22.1, REAPER 7.36, Wine 9.21 Staging, yabridge 5.1.1, VST2 and VST3 | [#419](https://github.com/robbert-vdh/yabridge/issues/419) (open) |
| 2025-04-17 | Vendor's own answer in that thread: 'modern Windows software requires Direct2D feature set v1.3 or up, while Wine only supports Direct2D up to v1.2. This is why you see a black screen' | any host | [#419](https://github.com/robbert-vdh/yabridge/issues/419), quoted by the reporter |
| 2025-05-08 | Binaries confirmed to be JUCE 8, which puts this under the JUCE 8 Direct2D bug | any host | [#419](https://github.com/robbert-vdh/yabridge/issues/419) (lechouette, after relaborn's `strings` check) |
| 2025-09-30 | 'ToneBoosters now have linux versions of the majority of their plugins. They work well.' | native | [#419](https://github.com/robbert-vdh/yabridge/issues/419) (relaborn; seconded by untilde 2026-02-10) |
| 2026-08-10 | Vendor ships a Linux plugin archive, v2.1.8 (July 2026) | native, VST and VST3 | [toneboosters.com](https://www.toneboosters.com/) |

---

[Back to the tracker index](../README.md) · [How to correct this page](../CONTRIBUTING.md)
