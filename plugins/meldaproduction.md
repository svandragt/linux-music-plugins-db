# MeldaProduction

*Status: verified · last checked 2026-08-10*

[Vendor page](https://www.meldaproduction.com/) · [All plugins](../README.md)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Works. Rendering is the weak spot: turn off the plugins' own GPU acceleration.

## Caveats and fixes

- With GPU acceleration on: missing redraws, and wrong positioning when the window is dragged off the top or left edge — the positioning half is fixed on yabridge master, unreleased.
- CPU use is higher than the same plugins on Windows.
- Older crash reports: MSoundFactory in REAPER (#144), MComb in Carla (#126).

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2021-11-03 | Page fault with MSoundFactory | REAPER | [#144](https://github.com/robbert-vdh/yabridge/issues/144) (closed, reported by JonathanTroyer) |
| 2021-08-05 | MComb crashing the host | Carla | [#126](https://github.com/robbert-vdh/yabridge/issues/126) (closed, reported by SquidRoe) |
| 2026-08-10 | GPU acceleration rendering issues; offscreen positioning fix | any host | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes), [CHANGELOG](https://github.com/robbert-vdh/yabridge/blob/master/CHANGELOG.md) |
