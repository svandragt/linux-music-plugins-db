# FabFilter

*Status: verified · last checked 2026-08-10*

[Vendor page](https://www.fabfilter.com/) · [All plugins](../README.md)

Runs under yabridge. Long-standing community favourite for bridged use; one open crash report in REAPER.

## Caveats and fixes

- VST2 instances that share data between each other (Pro-Q 3) must be hosted in one process — set up a plugin group.
- Not needed for the VST3 versions, which always share a process.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2024-08-28 | Crash with FabFilter plugins, suspected host latency change | REAPER | [#364](https://github.com/robbert-vdh/yabridge/issues/364) (open, reported by sidoka-contact) |
| 2026-08-10 | Plugin-group requirement for data-sharing VST2 instances | any host | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes) |
| 2026-08-10 | Listed as working by forum posters | unspecified | [Gearspace thread](https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) — snippet only, thread not opened |
