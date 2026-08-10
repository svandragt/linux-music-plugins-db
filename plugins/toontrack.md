[yabridge compatibility tracker](../README.md) › Toontrack (Superior Drummer 3, EZdrummer, EZkeys)

# Toontrack (Superior Drummer 3, EZdrummer, EZkeys)

*Status: reported, mixed · last checked 2026-08-10*

[Vendor page](https://www.toontrack.com/)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

The plugins load and play, but the interface is where they fall over. Three
separate reporters describe Superior Drummer 3 freezing or losing its drop-down
menus, in three different environments and across two Wine generations. EZkeys 2
and EZdrummer 3 are less severe: the EZkeys 2 redraw problem is a DXVK
installation problem with a known fix.

## Caveats and fixes

- EZkeys 2 not redrawing after a click is the DXVK case from yabridge's known
  issues, but installing the distribution package is not enough on its own — the
  reporter had to run DXVK's own `setup_dxvk.sh install` (or
  `winetricks dxvk`) inside the prefix before `winecfg` listed the libraries.
  DXVK is per-prefix, so repeat it for every prefix you use.
- Dragging a sample from a file manager into EZdrummer 3 does not work; dragging
  out of the plugin into the host does. This affects Wine plugins generally, not
  just Toontrack. Symlink your sample folder into the Wine prefix instead.
- Superior Drummer 3.0.1 (32-bit VST2) freezes REAPER on load. The reporter was
  told updating SD3 fixes it, but could not update.
- Old yabridge fixes cover part of this: the Superior Drummer 3 editor race in
  Bitwig Studio was fixed in yabridge 1.1.3 (2020), EZdrummer producing no sound
  in 3.0.0 (2021). Neither is the same bug as the reports above.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2026-07-29 | Superior Drummer 3 frozen on 'did not find any sound library' after moving from Wine 9.21 to Wine 11.0 | Linux Mint 22.3, REAPER 7.56, yabridge 5.1.1, VST2 and VST3 | [#493](https://github.com/robbert-vdh/yabridge/issues/493) (open, reported by chunkyandkoko) |
| 2026-02-25 | Superior Drummer 3 drop-down menus unresponsive; audio plays | Arch, REAPER, Wine 9.21, yabridge 5.1.1, VST3, Hyprland | [#467](https://github.com/robbert-vdh/yabridge/issues/467) (open, reported by sclewis900) |
| 2024-10-04 | Superior Drummer 3.0.1 freezes REAPER on load; fine standalone | Debian 12, REAPER 7.22, Wine 9.18 Staging, yabridge 5.1.0, 32-bit VST2 in a Bottles prefix | [#373](https://github.com/robbert-vdh/yabridge/issues/373) (open, reported by CaptainKeys21; same symptom reported by thiagonasper 2024-10-22 on Wine 8.0) |
| 2025-03-08 | EZkeys 2 GUI only redraws on window resize; fixed by installing DXVK into the prefix with `setup_dxvk.sh install` | Arch, yabridge 5.1.1 | [#410](https://github.com/robbert-vdh/yabridge/issues/410) (closed, reported by cleinias) |
| 2024-08-19 | Drag-and-drop from a file manager into EZdrummer 3 does nothing; drag out works | Fedora 39, Ardour and REAPER, Wine 9.8 Staging, yabridge 5.1.0, VST3 | [#362](https://github.com/robbert-vdh/yabridge/issues/362) (open, reported by jbmestelan; seconded by relaborn 2024-12-17 across REAPER, Mixbus and Bitwig) |
| 2020-05-12 | Superior Drummer 3 editor race in Bitwig Studio fixed in yabridge 1.1.3 | Bitwig Studio | [yabridge CHANGELOG](https://github.com/robbert-vdh/yabridge/blob/master/CHANGELOG.md) |
| 2021-02-14 | EZdrummer producing no sound, caused by the plugin assuming `effMainsChanged()` runs on the GUI thread, fixed in yabridge 3.0.0 | any host | [yabridge CHANGELOG](https://github.com/robbert-vdh/yabridge/blob/master/CHANGELOG.md) |

---

[Back to the tracker index](../README.md) · [How to correct this page](../CONTRIBUTING.md)
