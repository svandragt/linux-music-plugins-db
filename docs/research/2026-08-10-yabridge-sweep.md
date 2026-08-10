# Research record — yabridge sweep, 2026-08-10

Full evidence behind the [journal entry](../../JOURNAL.md) of the same date.
Nothing here has been applied to the table in `README.md` yet.

Reference points:

- yabridge master at `b580a9f7fc46509767ca156d4f92872552b9e571` (2026-08-02).
- Latest **release** is 5.1.1 (2024-12-23). Anything below marked *master* is
  committed but unreleased, so users on a distro package do not have it.

## 1. Source inventory and reachability

Read in full (authoritative, quoted directly below):

| Source | How |
| --- | --- |
| [yabridge README, "Known issues and fixes"](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes) | shallow clone of master |
| [yabridge CHANGELOG](https://github.com/robbert-vdh/yabridge/blob/master/CHANGELOG.md) | shallow clone of master |
| [wine-d2d1-dcomp README](https://github.com/mklnln/wine-d2d1-dcomp) | raw.githubusercontent |
| Issues [#354](https://github.com/robbert-vdh/yabridge/issues/354), [#386](https://github.com/robbert-vdh/yabridge/issues/386), [#476](https://github.com/robbert-vdh/yabridge/issues/476), [#478](https://github.com/robbert-vdh/yabridge/issues/478), plus the open and closed issue indexes | fetched github.com HTML |

Unreachable from the research environment — **blocked egress**, so every claim
traced to them below is from a search-engine snippet and must be re-checked
before use:

`gearspace.com` · `linuxmusicians.com` · `kvraudio.com` · `forum.juce.com` ·
`deepwiki.com` · `interfacinglinux.com` · `meow.garden` · `litui.ca`

Reddit is unreachable both ways — blocked to the search crawler and to direct
fetches — so the r/linuxaudio and r/linux_gaming angle of the brief could not be
covered beyond the Native Instruments thread already cited in the table.

Deliberately not used as evidence: `yabridge.org` and its testimonials page.
Unattributed marketing copy, per the sourcing rule in `CONTRIBUTING.md`.

## 2. yabridge known-issues, entry by entry

Everything in the upstream section, including entries that duplicate rows we
already have. Method is yabridge + Wine throughout. "Host" is only listed where
upstream names one.

| Plugin / vendor | Host | Outcome | Fix as documented upstream |
| --- | --- | --- | --- |
| Any plugin with missing/invisible/misaligned text | — | caveat | install `corefonts` or `allfonts` via winetricks |
| Recent JUCE-based plugins, GUI never redraws | — | caveat | install [DXVK](https://github.com/doitsujin/dxvk) plus Vulkan drivers; WineD3D no longer redraws |
| Several JUCE plugins, mouse cursor disappears | — | caveat | mouse over the resize handle in the bottom-right corner |
| **Serum 1** | — | works with fixes | disable `d2d1.dll` in winecfg, install `gdiplus` via winetricks, and uncheck "Show help tooltips" in global settings |
| **Native Instruments** (incl. Kontakt) | — | works, install pain | Native Access 2.x needs work under Wine ([WineHQ appdb](https://appdb.winehq.org/objectManager.php?sClass=version&iId=41820)); legacy Native Access 1.x installs directly with winecfg reporting Windows 10; "Error while mounting disk image" needs `udisksctl loop-setup` then `udisksctl mount -t udf -o unhide`, and older distros need `udf_allow=…,unhide,…` in `/etc/udisks2/mount_options.conf` |
| **Spitfire Audio** (BBC Symphony Orchestra, LABS) | — | caveat | sample libraries fail with *Error #X: Something went wrong*; reinstall into a new clean Wine prefix after uninstalling from the main one |
| **Arturia** plugins, Sonic Academy **Kick 2**, Cytomic **The Drop** (JUCE) | — | caveat | GUI freezes when drawing a tooltip; enable "Hide Wine version from applications" in the winecfg Staging tab. Upstream note: if a plugin works but freezes on click, try this option |
| **Sforzando** (Plogue) | — | cosmetic only | GUI looks unresponsive to clicks but is actually updating; drag the window or click anywhere to force a redraw |
| **MeldaProduction** | — | caveat | minor rendering issues with GPU acceleration — disable it in plugin settings. Missing redraws and wrong positioning when dragged offscreen top/left |
| **Tokyo Dawn Records** (covers TDR Nova) | — | caveat | knobs misbehave on long drags; set "Continuous Drag" to "Linear" |
| **Voxengo** | — | caveat | enable "Radial knob mode" in global settings |
| **Scaler 2** | — | caveat | interface lags/blacks out/renders poorly; enable [software rendering](https://forum.scalerplugin.com/t/scaler-2-black-empty-window/3540/8) |
| **ujam** and other Gorilla Engine plugins, e.g. **Loopcloud** | — | caveat | `JS_EXEC_FAILED` on load; enable the `disable_pipes` compatibility option |
| **KiloHearts** | — | caveat | file-descriptor leaks under *esync* until the open-file limit is hit; unset `WINEESYNC` or switch to *fsync* |
| **PSPaudioware**, **Soundtoys** (E27, Crystallizer) | — | caveat | expandable GUI appears in the wrong place after expanding; enable the alternative editor hosting mode |
| **Applied Acoustics Chromaphone 3** | Bitwig Studio | caveat | text entry crashes because Chromaphone switches text-entry method when it detects Bitwig; enable `hide_daw` |
| **FabFilter Pro-Q 3** (VST2) | — | caveat | cross-instance data sharing needs all instances in one process; use plugin groups. Not needed for VST3 |
| VST3 modules never unloaded | Ardour, REAPER, Qtractor | caveat | `yabridge-host.exe` lingers until the project closes; REAPER has "Allow complete unload of VST plug-ins" |
| Drag-and-drop into the plugin window | REAPER | broken upstream | long-standing REAPER FX-window issue; use the `editor_force_dnd` compatibility option |
| **iZotope** | — | **confirmed broken** | cannot be authorized — missing functionality in Wine's crypt32. No fix |
| **D16 Group** | — | **confirmed broken** | cannot be authorized in current Wine; authorization status not recalled correctly |
| **Waves V13 VST3** | — | **confirmed broken / unstable** | memory issues under Wine, will likely crash randomly; prefer V12 if licensed. Upstream advice is to avoid Waves |
| MIDI key labels (VST2) | — | protocol limit | never refresh after the host's first query; deactivate and reactivate the plugin |

Upstream troubleshooting also states plainly: **Wine 9.22 and Wine 10.x do not
work with yabridge 5.1.1 or below.** Downgrade to Wine 9.21 or install a
development build.

## 3. CHANGELOG, plugin- and host-relevant entries

**Unreleased (on master as of 2026-08-02)**

- Wine 9.22+ compatibility fix — mouse clicks in plugin GUIs did not register.
- Worked around an Ubuntu 24.10 interaction with hosts like **Ardour** where
  yabridge would hang and crash the host by consuming memory. Affected the
  prebuilt release binaries only.
- More VST3 functions now called from the UI thread, for plugins on modern
  VSTGUI versions "such as *Serum 2*".
- Side effect of the above: GUIs no longer offset when dragged offscreen on the
  top/left edges.
- Popups no longer appear in the wrong place — "mostly affected
  *MeldaProduction*".
- **Removed**: `editor_xembed` (broken for several Wine releases),
  `editor_coordinate_hack`, and out-of-the-box 32-bit builds
  ([#431](https://github.com/robbert-vdh/yabridge/issues/431); only mattered for
  32-bit Linux **EnergyXT**).

**5.1.1 (2024-12-23)** — DPI scaling fix for Wine 9.17+ font DPI scaling;
segfault on unload.

**5.1.0 (2023-12-23)** — exports `yabridge_version` so hosts can detect
yabridge; **Ardour 8.2** uses it to fix an Ardour 7.3 regression that froze some
VST3 plugins. **Renoise** VST2 DPI-scaling freeze fixed.

**5.0.5 (2023-05-07)** — VST3/CLAP parameter info queried in one batch, fixing
slow **Kontakt** patch loading in **REAPER**; **Audio Nebula Aurora FM** window-
drag flicker; **PolyChrome DSP McRocklin Suite** recursive-callback deadlock.

**5.0.4 / 5.0.3 / 5.0.2** — Wine 8.0 version handling; Wine 7.21–8.0-rc
compatibility restored; **Audio Nebula Aurora FM** slow redraws on window drag.

## 4. Issue tracker

| Issue | State / date | Content |
| --- | --- | --- |
| [#497](https://github.com/robbert-vdh/yabridge/issues/497) | open, 2026-08-06 | **Arturia** VST3 GUI hitbox / mouse misalignment on Wayland + KDE |
| [#488](https://github.com/robbert-vdh/yabridge/issues/488) | open | VST3 editor crashes with **Wine 11.12** on **KDE Plasma 6** |
| [#476](https://github.com/robbert-vdh/yabridge/issues/476) | open, 2026-04-27 | **Serum 2** no GUI: **Bitwig 6.0**, Wine Staging 11.7, yabridge 5.1.1-7. Loads and plays via MIDI; popout window is black and non-interactive; Bitwig's inline device controls still work. Reporter found #413's advice unclear/inapplicable. No workaround in thread |
| [#472](https://github.com/robbert-vdh/yabridge/issues/472) | closed 2026-06-28 | **REAPER** stops redrawing its UI on GNOME / NVIDIA |
| [#479](https://github.com/robbert-vdh/yabridge/issues/479) | closed 2026-05-21 | **VOCALOID6** editor not showing up. Closing reason not retrieved |
| [#478](https://github.com/robbert-vdh/yabridge/issues/478) | closed 2026-05-02 | "Is it possible to get **Waves Clarity** to work?" — question only, no versions, no outcome, no resolution recorded. **Not usable as evidence** |
| [#446](https://github.com/robbert-vdh/yabridge/issues/446) | — | yabridgectl doesn't sync new plugins |
| [#413](https://github.com/robbert-vdh/yabridge/issues/413) | open, 2025-03-19 | **Serum 2** graphical issues — the earlier of the two Serum 2 reports |
| [#409](https://github.com/robbert-vdh/yabridge/issues/409) | — | Wine 9.22 / Wine 10 editor embedding, tracking issue |
| [#392](https://github.com/robbert-vdh/yabridge/issues/392) | closed 2026-01-13 | yabridge can't find Wine in **Bitwig** on **Pop!_OS** |
| [#386](https://github.com/robbert-vdh/yabridge/issues/386) | opened 2024-12-18, closed 2026-06-04 | **JUCE 8 black screen and crash** — see below |
| [#382](https://github.com/robbert-vdh/yabridge/issues/382) | — | mouse cursor offset, Wine 9.22+ |
| [#377](https://github.com/robbert-vdh/yabridge/issues/377) | open, 2024-10-20 | yabridge broken on **Kubuntu 24.10** in **Ardour**, **Bitwig Studio** and **PreSonus Studio One** |
| [#355](https://github.com/robbert-vdh/yabridge/issues/355) | closed 2026-03-01 | "Running any **Spectral Suite** plugins crashes". Closing reason not retrieved |
| [#354](https://github.com/robbert-vdh/yabridge/issues/354) | open, 2024-07-16 | **Bitwig 5.1.9 / 5.2 Beta 11** stopped loading yabridge plugins during indexing from ~July 2024 — "Plugin host did not respond for 20.0 seconds" reading metadata. Affects VST2, VST3 and CLAP, **Arturia**, **Cherry Audio** and free plugins. Fresh Bitwig install and full yabridge/Wine reinstall did not help. Unresolved |
| [#32](https://github.com/robbert-vdh/yabridge/issues/32) | historical | plugins crash the host when switching patch/preset |

### #386 in detail — the JUCE 8 / Direct2D 1.3 wall

Reported on yabridge 5.1.1, Wine 9.21 (TkG Staging, esync/fsync), Mesa 22.3.6.
JUCE 8 targets **Direct2D feature level 1.3**, which is not available in Wine,
DXVK or VKD3D; stock Wine also lacks `dcomp.dll`'s `DCompositionCreateDevice`.
Symptom is a black GUI and a crash, with
`DxgiFactory::CreateSwapChainForComposition: Not implemented` in the log.

- **Broken**: Audio Modeling **SWAM** instruments and **Ambiente**, **Hertz
  Drums**, **Aberrant DSP** (all), **VocAlign 6 Pro** (Synchro Arts).
- **Working despite JUCE 8**: Minimal Audio **Squash**, apulSoft **apUnmask** —
  these detect Wine and fall back to the older renderer.
- Hosts named: **Bitwig**, **REAPER**, **Mixbus**.
- Fix path is per-vendor: detect Wine, fall back. apulSoft has done this.
  Otherwise downgrade to a JUCE 7 build of the plugin.
- **The closing comment could not be retrieved**, so it is unknown whether
  2026-06-04 marks a fix, a Wine-side resolution, or housekeeping. Do not state
  that it was fixed without checking.

Corroborating, outside yabridge: [Wine bug
57833](https://list.winehq.org/hyperkitty/list/wine-bugs@list.winehq.org/message/VINNBRTJCXRSDT4IVS5HZODD753JMBXT/)
"JUCE 8 incompatibility", the JUCE forum thread [Juce8 Direct2D
WINE/yabridge](https://forum.juce.com/t/juce8-direct2d-wine-yabridge/64298), and
WineHQ forum threads [42178](https://forum.winehq.org/viewtopic.php?t=42178) and
[39700](https://forum.winehq.org/viewtopic.php?t=39700).

### wine-d2d1-dcomp — the patched-Wine route

[mklnln/wine-d2d1-dcomp](https://github.com/mklnln/wine-d2d1-dcomp) patches Wine
for Direct2D 1.3 and DirectComposition to fix black JUCE 8 GUIs, on Arch and
CachyOS, tracking giang17's `d2d1-dcomp-11.0` branch. Notes that **Wine-Staging
11.6** added DirectComposition but still lacks Direct2D 1.3.

- Confirmed working on the patched build: **Pianoteq 9** VST3 bridged into
  **Bitwig** (though it recommends Pianoteq's native Linux build), and **Serum
  2**, which it describes as broken on stock Wine.
- Fine on stock Wine: **Minimal Audio Squash**, **apulSoft apUnmask**.
- Only **Bitwig** is named as tested.

## 5. Snippet-only claims

Search-engine snippets from blocked domains. Recorded so the leads are not lost;
**not** citable evidence in this state. Each needs the thread opened, the poster
and date noted, before it can back a table row.

| Claim | Apparent source |
| --- | --- |
| Melda "works very smoothly", good results with TurboReverb, MPowerSynth, MSoundFactory; Fedora with Wine 9.21 + yabridge; CPU notably higher than Windows; popups may need Wine's virtual desktop | [KVR "Melda on Linux – community reports"](https://www.kvraudio.com/forum/viewtopic.php?t=623309) |
| FabFilter works via yabridge (2025); Soundtheory **Gullfoss** works | [KVR "Running commercial audio software on linux"](https://www.kvraudio.com/forum/viewtopic.php?t=503359) |
| iZotope + yabridge fails | [KVR "Yabridge and Izotope trash"](https://www.kvraudio.com/forum/viewtopic.php?t=571462) |
| **Omnisphere** in 2025: "very mixed bag" — great for some, a "neverending fight" for others | [LinuxMusicians t=27992 / t=27991](https://linuxmusicians.com/viewtopic.php?t=27992) |
| Serum, FabFilter and Kontakt "work flawlessly" in REAPER; typical stack is Reaper + yabridge + Wine-staging + wineasio from KX-Studio | KVR / LinuxMusicians threads above |
| **Morph 2**, **Kontakt** and **Valhalla Room** all fine with yabridge in Bitwig | [litui.ca "Music-making in Linux with Bitwig and Yabridge"](https://litui.ca/music-in-linux/) |
| Aug 2025: Xfer added config keys to make Serum behave under Wine's partial Direct2D, notably disabling DirectComposition; resulting UI slow and buggy | [meow.garden "Serum 2 works* on Linux now"](https://meow.garden/serum-2-linux/) |
| Feb 2026: giang17 began publishing Direct2D patches against Wine 11.0, validated by several users in the Serum 2 mega-issue | meow.garden, JUCE forum |
| Not every JUCE 8 plugin breaks — only those using the new D2D/DComp path with no Wine fallback | JUCE forum 64298 |
| Bridges are effectively pinned to Wine 9.21 while Wine moves from X11 to Wayland | KVR 503359 |
| Audio Modeling's own software centre also misdraws on Linux; their support suspects the JUCE 8 upgrade | JUCE forum 64298, [VI-Control 159619](https://vi-control.net/community/threads/reaper-linux-audio-modeling.159619/) |
| Arturia install walkthrough for Linux | [dev.to](https://dev.to/neroblackstone/install-arturia-vst-on-linux-22i9) |

## 6. Proposed table changes

The reviewable summary, unchanged from what was reported in session. Statuses
follow the `CONTRIBUTING.md` rule — `verified` only where two or more
independent, *readable* sources agree.

### Status changes

| Row | Proposed | Basis |
| --- | --- | --- |
| Serum (Xfer) | split: **Serum 1** `verified` with fixes; **Serum 2** `confirmed broken` on stock Wine, works on patched Wine | upstream known-issues, #413, #476, CHANGELOG unreleased, wine-d2d1-dcomp |
| Kontakt (NI) | `reported` → `verified`, caveat: Native Access install | upstream NI section, CHANGELOG 5.0.5 |
| MeldaProduction | `reported` → `verified`, caveat: disable GPU acceleration | upstream, CHANGELOG unreleased (+ KVR thread once opened) |
| TDR Nova | `reported` → `verified`, caveat: Continuous Drag = Linear | upstream, existing Gearspace citation |
| UAD / Waves / Plugin Alliance | split **Waves V13 VST3** out as `confirmed broken` | upstream caveats, existing Gearspace rollback story |
| iZotope | stays `confirmed broken`, second source added | upstream, KVR 571462 (snippet) |

### New rows — verified

| Row | Status | Basis |
| --- | --- | --- |
| JUCE 8 plugins needing Direct2D 1.3 (SWAM/Ambiente, Aberrant DSP, Hertz Drums, VocAlign 6 Pro) | `confirmed broken` | #386, Wine bug 57833, JUCE forum 64298, wine-d2d1-dcomp |
| Arturia | `verified`, caveats | upstream, #497, #354 |
| Minimal Audio Squash, apulSoft apUnmask | `verified` | #386, wine-d2d1-dcomp |

### New rows — reported (single source)

Spitfire Audio · Sonic Academy Kick 2 · Cytomic The Drop · Plogue Sforzando ·
Voxengo · Scaler 2 · ujam / Gorilla Engine / Loopcloud · **D16 Group**
(`confirmed broken`) · Cherry Audio · Audio Nebula Aurora FM · PolyChrome DSP
McRocklin Suite · Pianoteq 9 · Spectrasonics Omnisphere (mixed) · Soundtheory
Gullfoss.

### Host and environment notes

Better as a second table than as plugin rows: the Wine 9.22–11.x incompatibility
with released 5.1.1; Ubuntu/Kubuntu 24.10 with Ardour, Bitwig and Studio One;
Ardour 7.3–8.1 VST3 freezes fixed via Ardour 8.2; REAPER VST3 unload and
drag-and-drop; Wine 11.12 on KDE Plasma 6; and the removal of `editor_xembed`
and `editor_coordinate_hack`.

## 7. Open questions for the next pass

1. Why was [#386](https://github.com/robbert-vdh/yabridge/issues/386) closed on
   2026-06-04? This decides whether JUCE 8 stays `confirmed broken`.
2. Same for [#355](https://github.com/robbert-vdh/yabridge/issues/355) (Spectral
   Suite) and [#479](https://github.com/robbert-vdh/yabridge/issues/479)
   (VOCALOID6) — both closed in 2026 with the reason unread.
3. Has anything shipped after 5.1.1? Users on distro packages still hit the Wine
   9.22+ click bug, which shapes almost every current report.
4. Open the snippet-only threads in section 5 from an unblocked network — that
   alone would promote Valhalla Room, Melda, Gullfoss and Omnisphere.
5. Cover Reddit (r/linuxaudio, r/linux_gaming) and Mastodon, both missed here.
6. Are the Serum 2 Wine patches heading for Wine-Staging? If so, several
   "broken" rows become version-bound rather than broken.
