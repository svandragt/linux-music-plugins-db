# yabridge compatibility tracker

*unofficial · crowd-sourced · not affiliated with yabridge*

There's no ProtonDB for yabridge. This is a manually compiled read of what's
floating around forums and the yabridge GitHub, cross-checked for how many
independent sources actually back each entry.

This table is an index. Each plugin has a page with the dated reports behind it,
the host DAW and Wine or yabridge versions involved, and the fixes that were
needed — the detail that would make this table unreadable.

## Read this first

**What this is:** second-hand reports, collected by hand, about software none of
the people here maintain. It is a starting point for your own testing, not a
compatibility guarantee.

**Where it will be wrong:**

- Nobody here retested these plugins. Almost every entry summarises what someone
  else wrote, often years ago. Every source now cited has been opened and read —
  two forum threads only through the Internet Archive, because the live sites are
  behind bot challenges. Where a claim could not be traced to a source that opens,
  it was withdrawn, and the page says so.
- Compatibility is version-bound and moves fast. A row is only about the Wine,
  yabridge, plugin and host versions named on its page — and a fix on yabridge's
  `master` branch is not in a release. Your combination is probably different.
- `verified` means two independent people reported the same thing. It does not
  mean anyone confirmed it on your distribution, your host, or your hardware.
- `confirmed broken` means broken in the reports we found. A vendor or Wine update
  may have fixed it since; a working plugin may have broken since.
- Check each page's *last checked* date before trusting it.

**Don't buy a plugin on the strength of a row here.** Use the vendor's trial, and
ask the vendor about Linux and Wine before paying. Very few of these vendors
support Wine at all, and using their plugins this way may fall outside their terms
— that is between you and them.

Not affiliated with, endorsed by, or speaking for yabridge, WineHQ, or any plugin
vendor named here. Product and brand names belong to their owners; they appear
only to identify what a report is about. No warranty, express or implied.

Found something wrong or out of date? That's the useful contribution — open an
issue or a pull request.

## Scope

**In scope:** Windows audio plugins running on Linux through a translation layer —
yabridge above all, and plain Wine or LinVst where a report covers them. That is
where the information is scattered, contradictory and undated, which is the only
reason this database earns its keep.

**Out of scope:** cataloguing native Linux plugins. Not because they don't matter
— they are usually the better answer — but because the question "does this ship a
Linux build?" already has an authoritative answer on the vendor's own page, and
the lists below already do the cataloguing:

- [Linux Audio applications index](https://wiki.linuxaudio.org/apps/all) — over
  1,500 indexed entries, alphabetical
- [awesome-linuxaudio](https://github.com/nodiscc/awesome-linuxaudio) — curated
  LV2, LADSPA and VST plugins alongside hosts and utilities

Nothing here needs two independent sources: a vendor either ships a Linux build or
it doesn't. Verification is for claims nobody official will make.

**Where the two meet:** when a plugin already in this table also has a native
Linux build of *the same product*, its page says so under **Native alternative**,
because the best outcome of landing on one of these rows is finding out you don't
need to bridge anything. That's a note on an existing row, not an invitation to
add rows for plugins that were never bridged.

## Legend

- **verified** — 2+ independent sources
- **reported** — single source only
- **confirmed broken** — does not work

A source is a report you can open and read: a GitHub issue, a forum post, a
CHANGELOG entry. yabridge's own README and CHANGELOG count as one source between
them, since they are one project's voice. Vendor testimonials are not sources.

## Plugins

| Plugin / brand | Last checked | Status |
| --- | --- | --- |
| [FabFilter](plugins/fabfilter.md) | 2026-08-10 | verified |
| [Neural DSP](plugins/neural-dsp.md) | 2026-08-10 | verified |
| [Kontakt (Native Instruments)](plugins/kontakt.md) | 2026-08-10 | verified |
| [KiloHearts](plugins/kilohearts.md) | 2026-08-10 | verified |
| [MeldaProduction](plugins/meldaproduction.md) | 2026-08-10 | verified |
| [Chromaphone 3 (Applied Acoustics)](plugins/chromaphone.md) | 2026-08-10 | verified |
| [Soundtoys / PSPaudioware](plugins/soundtoys-psp.md) | 2026-08-10 | verified |
| [Arturia](plugins/arturia.md) | 2026-08-10 | verified |
| [Sforzando (Plogue)](plugins/sforzando.md) | 2026-08-10 | verified |
| [Voxengo](plugins/voxengo.md) | 2026-08-10 | verified |
| [ujam / Gorilla Engine / Loopcloud](plugins/ujam-gorilla-engine.md) | 2026-08-10 | verified |
| [Serum 1 (Xfer Records)](plugins/serum-1.md) | 2026-08-10 | reported |
| [Brainworx / Plugin Alliance](plugins/brainworx.md) | 2026-08-10 | reported |
| [Valhalla Room](plugins/valhalla-room.md) | 2026-08-10 | reported |
| [Klanghelm](plugins/klanghelm.md) | 2026-08-10 | reported |
| [TDR Nova (Tokyo Dawn Records)](plugins/tdr-nova.md) | 2026-08-10 | reported |
| [Scaler 2](plugins/scaler-2.md) | 2026-08-10 | reported |
| [Sonic Academy Kick 2 / Cytomic The Drop](plugins/kick2-the-drop.md) | 2026-08-10 | reported |
| [Cherry Audio](plugins/cherry-audio.md) | 2026-08-10 | reported |
| [Vital](plugins/vital.md) | 2026-08-10 | reported |
| [Pianoteq 9 (Modartt)](plugins/pianoteq.md) | 2026-08-10 | reported |
| [Aurora FM / McRocklin Suite](plugins/aurora-fm-mcrocklin.md) | 2026-08-10 | reported |
| [Minimal Audio Squash / apulSoft apUnmask](plugins/squash-apunmask.md) | 2026-08-10 | reported |
| [Pulsar Audio](plugins/pulsar-audio.md) | 2026-08-10 | reported |
| [Toontrack (Superior Drummer 3, EZdrummer, EZkeys)](plugins/toontrack.md) | 2026-08-10 | reported, mixed |
| [Spire (Reveal Sound)](plugins/spire.md) | 2026-08-10 | reported, mixed |
| [DMG Audio](plugins/dmg-audio.md) | 2026-08-10 | reported, mixed |
| [UAD (native plugins)](plugins/uad-plugin-alliance.md) | 2026-08-10 | reported, mixed |
| [Spitfire Audio (BBC SO, LABS)](plugins/spitfire-audio.md) | 2026-08-10 | reported, mixed |
| [Serum 2 (Xfer Records)](plugins/serum-2.md) | 2026-08-10 | confirmed broken |
| [Omnisphere (Spectrasonics)](plugins/omnisphere.md) | 2026-08-10 | confirmed broken |
| [ToneBoosters](plugins/toneboosters.md) | 2026-08-10 | confirmed broken |
| [Waves V13 VST3](plugins/waves-v13-vst3.md) | 2026-08-10 | confirmed broken |
| [iZotope](plugins/izotope.md) | 2026-08-10 | confirmed broken |
| [D16 Group](plugins/d16-group.md) | 2026-08-10 | confirmed broken |
| [JUCE 8 plugins needing Direct2D 1.3](plugins/juce8-direct2d.md) | 2026-08-10 | confirmed broken |

## Hosts and Wine

Status often depends on the host and the Wine version rather than the plugin.

| Date | What breaks | Environment |
| --- | --- | --- |
| 2026-07-09 | VST3 editor crashes on close ([#488](https://github.com/robbert-vdh/yabridge/issues/488), open) | Wine 11.12, KDE Plasma 6 Wayland |
| 2026-06-28 | REAPER stops redrawing its UI ([#472](https://github.com/robbert-vdh/yabridge/issues/472), fixed) | GNOME, NVIDIA |
| 2025-03-01 | Mouse clicks don't register on Wine 9.22 through 11.x with released yabridge 5.1.1 — use Wine 9.21 or a dev build ([#409](https://github.com/robbert-vdh/yabridge/issues/409)) | any host |
| 2024-10-20 | Prebuilt binaries hang and eat memory until the host dies ([#377](https://github.com/robbert-vdh/yabridge/issues/377), fixed) | Ubuntu/Kubuntu 24.10 with Ardour, Bitwig, Studio One |
| 2024-07-16 | Bitwig gives up on indexing when a plugin scan is slow ([#354](https://github.com/robbert-vdh/yabridge/issues/354), fixed) | Bitwig |
| 2026-08-10 | VST3 modules stay loaded unless 'Allow complete unload of VST plug-ins' is on; drag-and-drop needs `editor_force_dnd` | REAPER, Ardour, Qtractor |

Reference point for everything above: yabridge's latest release is 5.1.1
(2024-12-23), so any fix described as landing on master is unreleased.

## Contributing

Edit the table above and the plugin's page, then open a pull request. Every claim
needs a source you can open. See [CONTRIBUTING.md](CONTRIBUTING.md) for the
status rules and how the page is built.

## Sources

- [yabridge — known issues and fixes](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes)
- [yabridge issue tracker](https://github.com/robbert-vdh/yabridge/issues)
- [yabridge CHANGELOG](https://github.com/robbert-vdh/yabridge/blob/master/CHANGELOG.md)
- [Gearspace: Linux-compatible hardware/software/plugins](https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html)

No centralized compatibility database exists for yabridge, so this list is
assembled by hand and will drift as Wine, yabridge and plugin versions change.
Each page carries the date it was last checked.
