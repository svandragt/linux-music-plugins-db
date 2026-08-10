[yabridge compatibility tracker](../README.md) › FabFilter

# FabFilter

*Status: verified · last checked 2026-08-10*

[Vendor page](https://www.fabfilter.com/)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Runs under yabridge. Long-standing community favourite for bridged use; one open crash report in REAPER.

## Caveats and fixes

- VST2 instances that share data between each other (Pro-Q 3) must be hosted in one process — set up a plugin group.
- Not needed for the VST3 versions, which always share a process.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2024-08-28 | Crash with FabFilter plugins, suspected host latency change | REAPER | [#364](https://github.com/robbert-vdh/yabridge/issues/364) (open, reported by sidoka-contact) |
| 2026-08-10 | Plugin-group requirement for data-sharing VST2 instances | any host | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes) |
| 2025-06-17 | 'Fabfilter plugins - work via Yabridge' | Zorin OS 17.3, REAPER, Wine 9.0 | [Gearspace thread](https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) post #1 (Ellery Daines), read via the [Internet Archive](https://web.archive.org/web/20260505044054/https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) |
| 2025-09-27 | Whole suite still working; menus in the CLAP versions render small | Zorin OS 17.3, REAPER, Wine 9.21 via Bottles | [Gearspace thread](https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) post #20 (same poster) |

---

[Back to the tracker index](../README.md) · [How to correct this page](../CONTRIBUTING.md)
