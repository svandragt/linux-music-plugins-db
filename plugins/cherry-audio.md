# Cherry Audio

*Status: reported · last checked 2026-08-10*

[Vendor page](https://cherryaudio.com/) · [All plugins](../README.md)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Implicated in Bitwig plugin-indexing timeouts alongside Arturia. Single source.

## Caveats and fixes

- Bitwig gives up on scanning if a plugin takes too long to report back.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2024-07-16 | Bitwig stopped loading yabridge plugins (indexing timeouts) | Bitwig | [#354](https://github.com/robbert-vdh/yabridge/issues/354) (closed 2024-07-18) |
