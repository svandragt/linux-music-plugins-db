# Neural DSP

*Status: verified · last checked 2026-08-10*

[Vendor page](https://neuraldsp.com/) · [All plugins](../README.md)

Works. The freeze that used to hit Darkglass on load was fixed in yabridge itself.

## Caveats and fixes

- Interaction problems reported in REAPER (#432, closed).
- Amp-sim GUIs are JUCE-based, so the general JUCE cursor and redraw workarounds apply — DXVK if the GUI stops redrawing.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2025-06-01 | Plugin could not be interacted with | REAPER | [#432](https://github.com/robbert-vdh/yabridge/issues/432) (closed, reported by idealemu) |
| 2026-08-10 | Darkglass freeze on load fixed | any host | [yabridge CHANGELOG](https://github.com/robbert-vdh/yabridge/blob/master/CHANGELOG.md) |
