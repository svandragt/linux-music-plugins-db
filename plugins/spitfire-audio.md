[yabridge compatibility tracker](../README.md) › Spitfire Audio (BBC SO, LABS)

# Spitfire Audio (BBC SO, LABS)

*Status: reported, mixed · last checked 2026-08-10*

[Vendor page](https://www.spitfireaudio.com/)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Sample-library loading failures are fixable by reinstalling into a clean Wine
prefix. The interface problems are not: three separate reporters describe BBC SO
or LABS as a black window or a scan that never finishes, and BBC SO has been
updated to JUCE 8, which puts it squarely under the
[JUCE 8 / Direct2D 1.3](juce8-direct2d.md) wall.

## Caveats and fixes

- For 'Error #X: Something went wrong', reinstall the Spitfire software into a fresh prefix — uninstall from the old one first.
- If the window is black rather than erroring, see the JUCE 8 / Direct2D entry.
- If the host hangs while scanning rather than after loading, that is the same
  JUCE 8 problem — enable your host's 'skip unresponsive plugins' option so the
  scan finishes.
- An older, pre-JUCE 8 build works if the vendor will give you one. Spitfire's
  documentation does not record the JUCE change, so ask directly.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2026-02-25 | BBC SO black screen | Arch, REAPER, Wine 9.21, yabridge 5.1.1, VST3 | [#467](https://github.com/robbert-vdh/yabridge/issues/467) (open, reported by sclewis900) |
| 2025-08-08 | Ardour's plugin scan hangs for minutes on BBC SO at full CPU; answered with 'BBC SO is now JUCE8', pointing at [#386](https://github.com/robbert-vdh/yabridge/issues/386) | Fedora 42, Ardour | [#443](https://github.com/robbert-vdh/yabridge/issues/443) (closed, reported by b2jammer) |
| 2026-02-25 | BBC SO has been updated to JUCE 8 in recent months, which the vendor's own documentation does not mention | any host | [#467](https://github.com/robbert-vdh/yabridge/issues/467) (pawel-ulita) |
| 2025-06-29 | 'Spitfire Labs doesn't work at all'; restated 2025-09-27 as a black plugin GUI | Zorin OS 17.3, REAPER, Wine 9.0–9.21 | [Gearspace thread](https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) posts #16 and #20 (Ellery Daines), read via the [Internet Archive](https://web.archive.org/web/20260505044054/https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) |
| 2026-08-10 | Clean-prefix fix for library loading errors | any host | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes) |

---

[Back to the tracker index](../README.md) · [How to correct this page](../CONTRIBUTING.md)
