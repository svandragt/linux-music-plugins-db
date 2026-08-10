# Audio Nebula Aurora FM / PolyChrome DSP McRocklin Suite

*Status: reported · last checked 2026-08-10*

[Vendor page](https://polychromedsp.com/) · [All plugins](../README.md)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Both needed yabridge-side fixes and then worked: a painfully slow redraw for Aurora FM, and latency changing during initialisation for McRocklin.

## Caveats and fixes

- Aurora FM redraw worked around in yabridge 5.0.2.
- McRocklin latency handling fixed in 5.0.5.
- Single source — yabridge's own CHANGELOG.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2026-08-10 | Redraw workaround (5.0.2) and latency fix (5.0.5) | any host | [yabridge CHANGELOG](https://github.com/robbert-vdh/yabridge/blob/master/CHANGELOG.md) |
