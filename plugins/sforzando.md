# Sforzando (Plogue)

*Status: verified · last checked 2026-08-10*

[Vendor page](https://www.plogue.com/products/sforzando.html) · [All plugins](../README.md)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Works. The GUI can look like it ignores mouse clicks, but that is a redraw problem — the state underneath is updating.

## Caveats and fixes

- Drag the window or click anywhere to force a redraw.
- A separate GUI-opening error was reported in #327 (closed).

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2024-04-02 | Error when opening the Sforzando GUI | unspecified | [#327](https://github.com/robbert-vdh/yabridge/issues/327) (closed, reported by jbmestelan) |
| 2026-08-10 | Redraw explanation and workaround | any host | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes) |
