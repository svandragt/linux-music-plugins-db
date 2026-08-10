# Serum 1 (Xfer Records)

*Status: reported · last checked 2026-08-10*

[Vendor page](https://xferrecords.com/) · [All plugins](../README.md)

Works once two Wine tweaks are in place. Single source: yabridge's own documentation.

## Caveats and fixes

- Disable `d2d1.dll` in `winecfg`.
- Install `gdiplus` through `winetricks`.
- Turn off 'Show help tooltips' in the global settings to avoid the tooltip freeze.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2026-08-10 | Documented fixes for Serum 1 | any host | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes) |
