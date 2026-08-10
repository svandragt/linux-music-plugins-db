# Minimal Audio Squash / apulSoft apUnmask

*Status: reported · last checked 2026-08-10*

[Vendor page](https://www.minimal.audio/products/squash) · [All plugins](../README.md)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Useful counter-examples: JUCE 8 plugins that do work, because both ship a Wine-detecting software-render fallback.

## Native alternative

apulSoft ships native Linux VST3 builds — apQualizr2's requirements name a *Linux
64-bit VST3 host*, and a Linux VST3 arrived in a 1.1.x update. Which apulSoft
plugins are covered isn't clear from outside, so check the vendor's system
requirements for the one you want before bridging it. Nothing native for Minimal
Audio Squash. Checked 2026-08-10 on [apulsoft.ch](https://apulsoft.ch/).

## Caveats and fixes

- Shows the JUCE 8 Direct2D breakage is a vendor build choice, not an inevitability.
- apUnmask vendor page: <https://www.apulsoft.ch/apunmask/>

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2024-12-18 | Named as working JUCE 8 plugins with a software-render fallback | Bitwig, REAPER | [#386](https://github.com/robbert-vdh/yabridge/issues/386) (closed, thread discussion) |

---

[All plugins](../README.md) · [How to correct this page](../CONTRIBUTING.md)
