# KiloHearts

*Status: verified · last checked 2026-08-10*

[Vendor page](https://kilohearts.com/) · [All plugins](../README.md)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Works, but leaks file descriptors when Wine's *esync* is enabled until the system hits its open-file limit and Wine stops working.

## Caveats and fixes

- Unset `WINEESYNC`, or switch to *fsync*.
- Knobs and sliders reported not tracking correctly (#417).
- Phase Plant did not load Windows-made project states (#210, closed).

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2025-04-13 | Knobs and sliders don't work correctly | unspecified | [#417](https://github.com/robbert-vdh/yabridge/issues/417) (open, reported by 10kmotorola) |
| 2022-11-03 | Phase Plant doesn't load saved states from Windows projects | Bitwig | [#210](https://github.com/robbert-vdh/yabridge/issues/210) (closed) |
| 2026-08-10 | esync file-descriptor leak and the fsync workaround | any host | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes) |
