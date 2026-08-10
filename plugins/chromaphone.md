# Chromaphone 3 (Applied Acoustics)

*Status: verified · last checked 2026-08-10*

[Vendor page](https://www.applied-acoustics.com/chromaphone-3/) · [All plugins](../README.md)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Works, except that text entry crashes it under Bitwig — the plugin picks a different text-entry path when it detects Bitwig.

## Caveats and fixes

- Enable the `hide_daw` compatibility option to work around it.
- Bitwig-specific; other hosts are unaffected.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2021-09-17 | Crash when removing Objeq Delay from the same track | unspecified | [#137](https://github.com/robbert-vdh/yabridge/issues/137) (closed, reported by jonaspeter) |
| 2026-08-10 | Bitwig text-entry crash and `hide_daw` workaround | Bitwig | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes) |

---

[All plugins](../README.md) · [How to correct this page](../CONTRIBUTING.md)
