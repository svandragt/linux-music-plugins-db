# Spitfire Audio (BBC SO, LABS)

*Status: reported, mixed · last checked 2026-08-10*

[Vendor page](https://www.spitfireaudio.com/) · [All plugins](../README.md)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Sample-library loading failures are fixable by reinstalling into a clean Wine prefix, but BBC SO has also been reported as a black screen, which looks like the JUCE 8 Direct2D problem instead.

## Caveats and fixes

- For 'Error #X: Something went wrong', reinstall the Spitfire software into a fresh prefix — uninstall from the old one first.
- If the window is black rather than erroring, see the JUCE 8 / Direct2D entry.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2026-02-25 | BBC SO black screen | unspecified | [#467](https://github.com/robbert-vdh/yabridge/issues/467) (open, reported by sclewis900) |
| 2026-08-10 | Clean-prefix fix for library loading errors | any host | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes) |

---

[All plugins](../README.md) · [How to correct this page](../CONTRIBUTING.md)
