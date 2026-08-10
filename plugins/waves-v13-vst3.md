# Waves V13 VST3

*Status: confirmed broken · last checked 2026-08-10*

[Vendor page](https://www.waves.com/) · [All plugins](../README.md)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Memory problems under Wine and random crashes. yabridge's own advice is to avoid Waves, or fall back to the V12 versions.

## Caveats and fixes

- V12 is the recommended fallback if you still hold a licence.
- Individual plugins also go undetected (#402).

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2025-02-15 | Single Waves plugin not being picked up | unspecified | [#402](https://github.com/robbert-vdh/yabridge/issues/402) (open, reported by pheerai) |
| 2026-04-30 | Asking whether Waves Clarity can be made to work | unspecified | [#478](https://github.com/robbert-vdh/yabridge/issues/478) (closed, reported by geextahslex) |
| 2026-08-10 | V13 VST3 memory issues, V12 recommended | any host | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes) |
