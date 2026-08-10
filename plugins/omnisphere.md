[yabridge compatibility tracker](../README.md) › Omnisphere (Spectrasonics)

# Omnisphere (Spectrasonics)

*Status: confirmed broken · last checked 2026-08-10*

[Vendor page](https://www.spectrasonics.net/products/omnisphere/)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Downgraded from `reported, mixed` on 2026-08-10, after the LinuxMusicians thread
was finally opened. It contains no report of Omnisphere working — one person
describing a frozen interface, one reply suggesting a Wine downgrade that is never
confirmed to have helped, and the rest of the thread arguing about alternatives.
The installer path also involves PowerShell, which is where the one yabridge issue
stalls.

## Caveats and fixes

- Correction, 2026-08-10: the 'mixed' reading came from a search snippet. The
  thread itself does not support it. Nobody in any opened source reports
  Omnisphere running acceptably under yabridge.
- Suggested but unconfirmed: downgrade to Wine Staging 9.21.
- DXVK makes it worse — the reporter says it 'kills the GUI completely'.
- There is no Omnisphere demo, so this is unusually hard for anyone to test.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2022-12-01 | Omnisphere error involving PowerShell.exe | unspecified | [#220](https://github.com/robbert-vdh/yabridge/issues/220) (closed, reported by mukundasik) |
| 2025-02-05 | GUI frozen most of the time, occasionally a preset can be chosen; tried Wine 7.20, 9.0, 9.21 and 10; DXVK kills the GUI outright | Zorin OS 17.2 Lite, Bitwig and Renoise, Wine Staging 10.0, yabridge 5.1.1 | [LinuxMusicians thread](https://linuxmusicians.com/viewtopic.php?t=27992) (sebasaturn), read via the [Internet Archive](https://web.archive.org/web/20250624220350/https://linuxmusicians.com/viewtopic.php?t=27992) |
| 2025-02-05 | Reply advising a downgrade to Wine Staging 9.21; no confirmation it worked | as above | [LinuxMusicians thread](https://linuxmusicians.com/viewtopic.php?t=27992) (bill80) |

---

[Back to the tracker index](../README.md) · [How to correct this page](../CONTRIBUTING.md)
