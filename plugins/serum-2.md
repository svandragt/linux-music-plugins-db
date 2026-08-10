# Serum 2 (Xfer Records)

*Status: confirmed broken · last checked 2026-08-10*

[Vendor page](https://xferrecords.com/products/serum-2) · [All plugins](../README.md)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Broken on stock Wine: the GUI is black while audio keeps working. Serum 2 needs Direct2D 1.3, which Wine does not implement.

## Caveats and fixes

- Two independent reporters, a year apart, describe the same failure.
- Partial results with Xfer's own Wine configuration keys; reported working on Wine patched with d2d1/dcomp support.
- Serum 1 is a separate entry — it works with fixes.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2025-03-19 | Serum 2 graphical issues | unspecified | [#413](https://github.com/robbert-vdh/yabridge/issues/413) (open, reported by drac-dot-gay) |
| 2026-04-27 | Serum 2 no GUI | Bitwig 6.0, Wine Staging 11.7, yabridge 5.1.1-7 | [#476](https://github.com/robbert-vdh/yabridge/issues/476) (open, reported by smallghostbigthot) |
| 2026-08-10 | Patched Wine adding Direct2D 1.3 and `dcomp.dll` | any host | [wine-d2d1-dcomp](https://github.com/mklnln/wine-d2d1-dcomp) |
