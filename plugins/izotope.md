[yabridge compatibility tracker](../README.md) › iZotope

# iZotope

*Status: confirmed broken · last checked 2026-08-10*

[Vendor page](https://www.izotope.com/)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Cannot be authorised: Wine's crypt32 implementation is missing what the iZotope authorisation needs. Without authorisation the plugins are unusable.

## Caveats and fixes

- Not a yabridge bug and not fixable from yabridge — it needs Wine work.
- Tonal Balance Control reported separately (#439, closed).

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2025-06-30 | iZotope Tonal Balance Control | unspecified | [#439](https://github.com/robbert-vdh/yabridge/issues/439) (closed, reported by durutti) |
| 2026-08-10 | Authorisation fails, missing Wine crypt32 functionality | any host | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes) |

---

[Back to the tracker index](../README.md) · [How to correct this page](../CONTRIBUTING.md)
