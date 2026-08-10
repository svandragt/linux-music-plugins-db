# 2026-08-10 — Second sweep: five new entries, and the snippet rows re-checked

Full evidence for the second research pass. The [journal entry](../../JOURNAL.md)
is the summary; this is the record. Companion to
[2026-08-10-yabridge-sweep.md](2026-08-10-yabridge-sweep.md) and
[2026-08-10-verification.md](2026-08-10-verification.md).

Two goals: find five plugins the table did not already cover, and open every
source that the previous pass could only see as a search-engine snippet.

## Method

- Listed the last 200 issues in the yabridge tracker with
  `gh issue list -R robbert-vdh/yabridge --state all --limit 200`, then read each
  candidate in full with `gh issue view`, including comments. Every claim below
  names the reporter and the date the tracker gives.
- Read `README.md` and `CHANGELOG.md` from `robbert-vdh/yabridge` at `master`
  (`b580a9f7fc46`, 2026-08-02) through `gh api`. Mapped every CHANGELOG line cited
  to the release heading above it, so the dates are release dates rather than
  guesses.
- Checked every vendor URL with `curl` before linking it. Several vendors reject
  the default curl user agent with 403, so a browser user agent was used.

## Reachability

Both forum threads that the previous pass could only see as snippets are now
behind bot challenges, and neither can be fetched directly:

| Source | Direct fetch | How it was read |
| --- | --- | --- |
| [Gearspace thread 1449241](https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) | HTTP 403, Cloudflare managed challenge | [Internet Archive snapshot, 2026-05-05](https://web.archive.org/web/20260505044054/https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html) — 362 KB, full thread, 16 posts on page 1 |
| [LinuxMusicians topic 27992](https://linuxmusicians.com/viewtopic.php?t=27992) | HTTP 200 but only an Anubis proof-of-work interstitial | [Internet Archive snapshot, 2025-06-24](https://web.archive.org/web/20250624220350/https://linuxmusicians.com/viewtopic.php?t=27992) — 90 KB, all 14 posts |

The archive copies are complete pages, not excerpts, so the snippet caveat is gone
from every page that carried it. One claim could not be rescued: the Pianoteq
'works bridged on patched Wine' line had no recorded URL at all, so there was
nothing to re-open. It has been withdrawn rather than left standing.

Vendor pages:

| URL | Result |
| --- | --- |
| `https://www.toneboosters.com/` | 200 with a browser UA (403 with curl's default) |
| `https://pulsar.audio/poseidon/` | 200 |
| `https://www.toontrack.com/` | 200 |
| `https://acondigital.com/products/extract-dialogue/` | 200 |
| `https://dmgaudio.com/` | 200 |
| `https://revealsound.com/` | DNS resolves to 92.205.2.206, then the connection times out. Linked anyway because the page needs a vendor link, but **not verified live from here** |

## New entries

### Toontrack — `reported, mixed`

Three separate reporters on Superior Drummer 3, in three environments, across two
Wine generations:

| Issue | Opened | Reporter | Environment | Symptom |
| --- | --- | --- | --- | --- |
| [#493](https://github.com/robbert-vdh/yabridge/issues/493) | 2026-07-29 | chunkyandkoko | Linux Mint 22.3, REAPER 7.56, Wine 11.0, yabridge 5.1.1 | Frozen on 'did not find any sound library'. Worked before on Wine 9.21 |
| [#467](https://github.com/robbert-vdh/yabridge/issues/467) | 2026-02-25 | sclewis900 | Arch, REAPER, Wine 9.21, yabridge 5.1.1, VST3, Hyprland | Drop-down menus unresponsive, audio fine |
| [#373](https://github.com/robbert-vdh/yabridge/issues/373) | 2024-10-04 | CaptainKeys21 | Debian 12, REAPER 7.22, Wine 9.18 Staging, 32-bit VST2, Bottles | SD3 3.0.1 freezes REAPER on load; fine standalone. thiagonasper reported the same on 2024-10-22 |

Other Toontrack products in the same tracker:

- [#410](https://github.com/robbert-vdh/yabridge/issues/410) (2025-03-07, cleinias,
  closed 2025-03-08) — EZkeys 2 only redraws on window resize. **Solved.** The
  distribution DXVK package was not enough; the reporter had to run
  `setup_dxvk.sh install` in the prefix before `winecfg` listed the libraries.
  relaborn's follow-up: DXVK is per-prefix, `winetricks dxvk` does it too.
- [#362](https://github.com/robbert-vdh/yabridge/issues/362) (2024-08-19,
  jbmestelan, open) — drag-and-drop from a file manager into EZdrummer 3 does
  nothing; drag out works. relaborn (2024-12-17) reports the same across REAPER,
  Mixbus and Bitwig, so it is a Wine-wide limitation. Workaround: symlink the
  sample folder into the prefix.

CHANGELOG, both old and both fixed:

- yabridge 1.1.3 (2020-05-12) — 'Fixes the editor for Superior Drummer 3 and the
  Roland Cloud synths in Bitwig Studio.'
- yabridge 3.0.0 (2021-02-14) — `effMainsChanged()` moved to the GUI thread,
  'fixes **EZdrummer** not producing any sound'.

Status reasoning: `reported, mixed`. Multiple independent reporters, but the
outcomes differ by product and by Wine version, and EZkeys 2 has a working fix.

### ToneBoosters — `confirmed broken` (bridged), with a native alternative

[#419](https://github.com/robbert-vdh/yabridge/issues/419) (2025-04-17, open;
opened by a since-deleted account). Black screen for all ToneBoosters plugins on
Linux Mint 22.1, REAPER 7.36, Wine 9.21 Staging, yabridge 5.1.1, VST2 and VST3.

The thread contains the vendor's own answer, quoted by the reporter:

> We are aware of an issue with Wine; modern Windows software requires Direct2D
> feature set v1.3 or up, while Wine only supports Direct2D up to v1.2. This is why
> you see a black screen.

relaborn suggested checking the framework version with
`strings TB_Morphit_v1.vst3 | grep 'JUCE v'`; lechouette confirmed JUCE 8 on
2025-05-08. That makes this the same failure as
[#386](https://github.com/robbert-vdh/yabridge/issues/386), the existing JUCE 8 /
Direct2D 1.3 entry.

Native alternative — checked live on 2026-08-10, the vendor's download section
offers, next to the Windows and macOS installers:

> Linux — Plugin archive v2.1.8 (July 2026) for Linux; requires a 64-bit DAW with
> VST or VST3 support; Intel or AMD SSE2 processor; glibc version 2.31 or up.

The link is `downloads/TB_Archive_v2.1.8_linux.tar.gz`. Two people in the issue say
the same: relaborn (2025-09-30) 'ToneBoosters now have linux versions of the
majority of their plugins. They work well.', untilde (2026-02-10) 'There is no
reason to use yabridge for them.'

This is exactly the same-product overlap the scope decision allows, so it gets a
`## Native alternative` section rather than a new row.

### Spire (Reveal Sound) — `reported, mixed`

Two independent reporters, two different walls, both graphics-stack rather than
audio:

- [#318](https://github.com/robbert-vdh/yabridge/issues/318) (2024-03-21,
  gearcoded, open) — black screen once Vulkan drivers are installed, on Kubuntu
  22.04, Bitwig 4.4.10, WineHQ 9.0, yabridge 5.0.3, VST3. Right-click menus and
  audio still work. Traced to
  `fixme:vulkan:X11DRV_vkCreateWin32SurfaceKHR Application requires child window
  rendering, which is not implemented yet!` and
  [WineHQ bug 45277](https://bugs.winehq.org/show_bug.cgi?id=45277). Workaround
  posted by the same reporter on 2024-04-21: build a prefix whose `d3d9.dll`,
  `d3d10core.dll`, `d3d11.dll` and `dxgi.dll` come from a prefix without Vulkan
  support, symlinking the rest. A commenter (aenaria) tried Wine-tkg with the
  child-window patches instead and yabridge then failed to start at all.
- [#296](https://github.com/robbert-vdh/yabridge/issues/296) (2023-12-29,
  TheGuyWhoo, closed next day) — 'error code 126: Module not found' on load,
  resolved by the reporter: the prefix needed `d2d1.dll`.

Status reasoning: two independent sources, but they describe different failures and
both found a way through, so `reported, mixed` rather than `verified`.

### Pulsar Audio — `reported`

[#426](https://github.com/robbert-vdh/yabridge/issues/426) (2025-05-06, 0CCULTIST,
open). Poseidon hangs Renoise indefinitely when a song containing it is loaded;
needs a `killall`, and there is no 'plugin failed' message, so the reporter found
the culprit by moving plugin folders out of the yabridge directory one at a time.

relaborn suggested iLok. untilde (2025-08-01) reports the same freeze with other
Pulsar plugins and with DMG Audio, worse in REAPER than Renoise, on Fedora KDE 42
with Wine 9.21 and DXVK — and states plainly that Pulsar does not use iLok, so the
iLok theory is unsupported.

Status reasoning: two people, but one thread, and the independence rule says a
single thread is a single source. `reported`.

### DMG Audio — `reported, mixed`

- [#367](https://github.com/robbert-vdh/yabridge/issues/367) (2024-09-06,
  kuchtamartin, open) — in Limitless and TrackControl only the first keypress
  registers when typing a value, on Gentoo with Bitwig and yabridge 5.1, both VST2
  and VST3. Explicitly 'Works as expected in REAPER'. relaborn confirmed on
  2024-10-04 for the VST3 versions and gave a workaround: set the value roughly
  with the mouse, then type into Bitwig's own device control.
- [#426](https://github.com/robbert-vdh/yabridge/issues/426) — untilde names DMG
  Audio alongside Pulsar in the freeze report above, without detail.
- CHANGELOG, yabridge 3.3.0 (2021-06-03): DMG VST3 plugins freezing in REAPER when
  the plugin resizes itself, and when restoring several instances at once, both
  fixed.

Status reasoning: works in one host, has a specific input bug in another.
`reported, mixed` is the honest label; the two sources are one issue thread plus a
CHANGELOG, which is not two independent voices.

## Re-checking the snippet rows

Everything below was previously sourced to 'snippet only, thread not opened'.
The Gearspace thread turns out to be one prolific tester — Ellery Daines, on Zorin
OS 17.3 with REAPER, moving between Wine 9.0, 9.21 and 10.11 in Bottles — plus a
handful of replies. That matters: several rows that read like community consensus
are one person's testing, which is why none of them were promoted.

| Page | Was | Now | What the thread actually says |
| --- | --- | --- | --- |
| Klanghelm | snippet | `reported` (unchanged) | Post #17 (2025-07-24) 'Klanghelm plugins work via Wine/bottles'; still listed working in the #20 round-up (2025-09-27); post #29 (2025-09-30) measures MJUC at about 0.7% CPU idle on both Linux and Windows, 7% vs 4% with the editor open |
| FabFilter | snippet | `verified` (unchanged) | Post #1 (2025-06-17) 'Fabfilter plugins - work via Yabridge'; post #20 adds that CLAP menus render small. Still `verified` on #364 plus this, which are independent |
| Brainworx / Plugin Alliance | snippet | `reported` (unchanged) | Post #16 (2025-06-29): bx_focusrite sc 'extremely buggy' on Wine 10.11 — cursor offset, GUI black when popped out. Edited 2025-06-30: 'now runs perfectly, after reverting back to Wine 9.21'. Post #18 (2025-08-23): other Brainworx plugins also fine on 9.21 |
| Valhalla Room | snippet | `reported` (unchanged) | Listed as working in the Wine 9.21 bottle, post #20 (2025-09-27). The 'second write-up naming it alongside Kontakt and Morph 2' claim had no source and is gone |
| UAD | snippet | `reported, mixed` (unchanged) | Post #20 lists UAD as non-functional, 'installer not installing or communicating with copied plugins for activation'. Post #24 (Surbitone, 2025-09-29) had UAD, Waves and all Plugin Alliance working via iLok machine auth, then dropped yabridge: 'performance and stability vs native Windows just isn't up to snuff'. Two people, one thread, so not promoted |
| Vital | snippet | `reported` (unchanged), claim corrected | Post #20 lists Vital under **NATIVE**, not among the bridged plugins. The 'reported working bridged' line was wrong and has been withdrawn |
| Pianoteq | snippet, no URL | `reported` (unchanged), claim withdrawn | Nothing to re-open. Replaced with post #13 (xabilon, 2025-06-20) listing Modartt Pianoteq and Organteq as Linux-native developers, plus the vendor page |
| Omnisphere | snippet | **`reported, mixed` → `confirmed broken`** | The LinuxMusicians thread contains no working report at all. See below |

### Omnisphere, downgraded

The thread is 14 posts. The substance:

- sebasaturn (2025-02-05) — 'I see the Gui and sometimes i can choose a Preset.
  Most of the Time the Gui is frozen.' Zorin OS 17.2 Lite, Bitwig and Renoise, Wine
  Staging 10.0, yabridge 5.1.1, after trying Wine 7.20, 9.0, 9.21 and 10, with a
  long winetricks list. 'dxvk kills the Gui completely'.
- bill80 (2025-02-05) — 'Please downgrade your wine to wine staging V9.21.' Never
  confirmed to have helped; the original poster does not reply.
- glowrak guy (2025-02-05) — points at a KVR thread and suggests AVLinux, REAPER
  and an older NVIDIA card, then recommends free alternatives. GuntherT later
  checks that KVR link and reports it contains nothing relevant.
- The remaining posts argue about whether recommending alternatives is helpful.

No post in the thread reports Omnisphere working. The 'mixed' status came from a
snippet and does not survive reading the source, so the entry is now
`confirmed broken`, with the caveat recorded on the page.

## Existing pages that gained evidence

- **Spitfire Audio** — added
  [#443](https://github.com/robbert-vdh/yabridge/issues/443) (2025-08-08, b2jammer,
  closed): Ardour's plugin scan hangs for minutes on BBC SO at full CPU, answered
  with 'BBC SO is now JUCE8'. Added pawel-ulita's note in #467 (2026-02-25) that
  BBC SO was updated to JUCE 8 without the vendor documenting it. Added the
  Gearspace reports on LABS (2025-06-29 'doesn't work at all', 2025-09-27 'black
  plugin GUI'). Three independent reporters now; status stays `reported, mixed`
  because the sample-library errors do have a fix.
- **Waves V13 VST3** — added the Gearspace licence-installer failure (post #20) and
  Surbitone's counter-report of Waves running via iLok machine auth (post #24).
  Status unchanged: neither post names a version, and the `confirmed broken` label
  is scoped to V13 VST3 as yabridge documents it.

## Leads not taken

Real reports, left out of the table this pass. Each is one issue by one reporter
unless noted — enough for a row, not enough to be worth one yet.

| Lead | Issue | Note |
| --- | --- | --- |
| Acon Digital Extract:Dialogue 2 | [#487](https://github.com/robbert-vdh/yabridge/issues/487) (2026-07-06, empireisstriking) | Black UI then the DAW crashes, Linux Mint, REAPER, Wine 9.21. No comments yet. Closest to making the cut |
| Line 6 Helix Native | [#396](https://github.com/robbert-vdh/yabridge/issues/396) (2025-01-20, samwcoulter) | Stack overflow |
| Analog Obsession | [#317](https://github.com/robbert-vdh/yabridge/issues/317) (2024-03-14, David-Else) | OpenGL plugins have no GUI |
| Wavesfactory Trackspacer 2.5 | [#300](https://github.com/robbert-vdh/yabridge/issues/300) (2024-01-02, TheGuyWhoo) | GUI does not redraw; DXVK does not help |
| Sonic Charge Microtonic | [#380](https://github.com/robbert-vdh/yabridge/issues/380) (2024-11-24, Taxicletter) | Carla will not load it |
| Positive Grid BIAS FX 2 | [#292](https://github.com/robbert-vdh/yabridge/issues/292), [#293](https://github.com/robbert-vdh/yabridge/issues/293) (2023-12-24) | Two issues, same reporter (a-parhom), so one source. Gearspace post #18 adds that BIAS Amp 2 works only with the prefix set to Windows XP |
| Adam Szabo Viper | [#452](https://github.com/robbert-vdh/yabridge/issues/452) (2025-10-30, acaxxx) | 4.6 GB RAM per instance |
| VPS Avenger 2 | [#341](https://github.com/robbert-vdh/yabridge/issues/341) (2024-05-11, jbmestelan) | Fails at initialisation |
| NI Guitar Rig 7 | [#374](https://github.com/robbert-vdh/yabridge/issues/374) (2024-10-10, Bulevardi68) | Memory leak. Separate product from the Kontakt row |
| XLN Audio Addictive Drums | Gearspace posts #16, #20 | Works, but must be installed with Wine rather than Bottles or activation sees two machines |
| Black Salt Audio Silencer | Gearspace posts #1, #18 | Direct2D 1.3 again. The vendor supplied an older 1.1.1 build that works; online activation only opened a browser on Wine 9.0 |
| Soundtheory Gullfoss | Gearspace posts #1, #20 | Works via yabridge, in an iLok prefix |

## Open questions

- Superior Drummer 3 spans Wine 9.18, 9.21 and 11.0 with three different symptoms.
  Whether these are one bug or three is not answerable from the tracker.
- Nobody has retested Omnisphere since February 2025. The suggested Wine 9.21
  downgrade is still unconfirmed either way.
- The Reveal Sound vendor site did not respond from this environment. Someone
  should confirm the product URL is still right.
- Gearspace page 2 of thread 1449241 was not read; the archive snapshot covers
  page 1. Anything after post #30 is unexamined.
