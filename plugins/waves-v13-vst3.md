[yabridge compatibility tracker](../README.md) › Waves V13 VST3

# Waves V13 VST3

*Status: confirmed broken · last checked 2026-08-10*

[Vendor page](https://www.waves.com/)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Memory problems under Wine and random crashes. yabridge's own advice is to avoid Waves, or fall back to the V12 versions.

## Caveats and fixes

- V12 is the recommended fallback if you still hold a licence.
- Individual plugins also go undetected (#402).
- Licensing is a separate wall from the VST3 memory bug: one poster could not get
  the licence installer to run at all, another had Waves authorised via iLok
  machine authorisation. Neither says which version, so the `confirmed broken`
  status stays scoped to V13 VST3 as yabridge documents it.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2025-02-15 | Single Waves plugin not being picked up | unspecified | [#402](https://github.com/robbert-vdh/yabridge/issues/402) (open, reported by pheerai) |
| 2026-04-30 | Asking whether Waves Clarity can be made to work | unspecified | [#478](https://github.com/robbert-vdh/yabridge/issues/478) (closed, reported by geextahslex) |
| 2025-09-27 | Listed as non-functional — 'licence installer can't be found' | Zorin OS 17.3, REAPER, Wine 9.0–9.21 via Bottles | [Gearspace thread](https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) post #20 (Ellery Daines), read via the [Internet Archive](https://web.archive.org/web/20260505044054/https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) |
| 2025-09-29 | Counter-report: had Waves running via iLok machine authorisation, alongside UAD and Plugin Alliance, before abandoning yabridge for stability | unspecified | [Gearspace thread](https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) post #24 (Surbitone) |
| 2026-08-10 | V13 VST3 memory issues, V12 recommended | any host | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes) |

---

[Back to the tracker index](../README.md) · [How to correct this page](../CONTRIBUTING.md)
