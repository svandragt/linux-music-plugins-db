[yabridge compatibility tracker](../README.md) › Brainworx / Plugin Alliance

# Brainworx / Plugin Alliance

*Status: reported · last checked 2026-08-10*

[Vendor page](https://www.plugin-alliance.com/)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Reported working, and the report is version-bound in a useful way: the same poster
found Brainworx plugins near-unusable on Wine 10.11 and fine after reverting to
Wine 9.21. No yabridge issue confirms or denies it. One poster, so `reported`.

## Caveats and fixes

- Wine 9.21 is the version the working reports use. On Wine 10.11 the same poster
  saw offset cursor response and a black GUI when the editor was popped out into a
  standalone window.
- Plugin Alliance installers are JUCE-based; if a recent one shows a black window, check the JUCE 8 / Direct2D entry.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2025-06-29 | bx_focusrite sc works but is 'extremely buggy' — cursor offset, GUI black when popped out | Zorin OS 17.3, Wine 10.11 | [Gearspace thread](https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) post #16 (Ellery Daines), read via the [Internet Archive](https://web.archive.org/web/20260505044054/https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) |
| 2025-06-30 | Edit to that post: 'bx_Focusrite sc now runs perfectly, after reverting back to Wine 9.21' | Zorin OS 17.3, Wine 9.21 | [Gearspace thread](https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) post #16 (same poster) |
| 2025-08-23 | 'Have now tested other Brainworx plugins and they also run fine on Wine 9.21' | Zorin OS 17.3, Wine 9.21 | [Gearspace thread](https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) post #18 (same poster) |

---

[Back to the tracker index](../README.md) · [How to correct this page](../CONTRIBUTING.md)
