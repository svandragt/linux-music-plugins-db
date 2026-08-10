# Kontakt (Native Instruments)

*Status: verified · last checked 2026-08-10*

[Vendor page](https://www.native-instruments.com/) · [All plugins](../README.md)

Works, but installing it is the hard part: Native Access 2.x needs Wine work, and libraries often have to be mounted and installed by hand.

## Caveats and fixes

- Native Access 1.x legacy installer is the easier route; set Windows 10 in `winecfg` or the installer hangs on an ISO driver.
- 'Error while mounting disk image' means mounting the library .iso yourself with `udisksctl ... -o unhide`.
- VST3 patch loading was slow in REAPER until yabridge 5.0.5 (2023-05-07).
- Render lag reported on the wine10-embedding branch (#469).

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2024-09-30 | Kontakt 7 crashing the DAW when opening the rack | unspecified | [#372](https://github.com/robbert-vdh/yabridge/issues/372) (closed, reported by sidoka-contact) |
| 2024-07-20 | Kontakt 7 crashes after installing DXVK | unspecified | [#356](https://github.com/robbert-vdh/yabridge/issues/356) (closed, reported by RichardJECooke) |
| 2026-03-09 | Bad performance and render lag | new-wine10-embedding branch | [#469](https://github.com/robbert-vdh/yabridge/issues/469) (open, reported by kernelPanic0x) |
| 2026-08-10 | Install procedure and Native Access notes | any host | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes) |
