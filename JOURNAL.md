# Journal

Dated notes on how this database changes and why: what was researched, what was
decided, and what is still unresolved. Newest entry first. Add an entry when you
change the pipeline or do a research pass — not for a single-row fix, which the
commit message covers on its own.

## 2026-08-10 — Second sweep: five new entries, and the snippet rows opened

Five plugins added, and every source the last pass could only see as a
search-engine snippet has now been read in full. 36 entries.

New: **Toontrack** (`reported, mixed` — three separate reporters on Superior
Drummer 3 across Wine 9.18, 9.21 and 11.0, plus EZkeys 2 and EZdrummer 3),
**ToneBoosters** (`confirmed broken` bridged, with a native Linux build the vendor
ships), **Spire** by Reveal Sound (`reported, mixed` — two reporters, two different
Direct3D/Direct2D walls, both with workarounds), **Pulsar Audio** (`reported` —
Poseidon hangs Renoise on song load with no error), **DMG Audio**
(`reported, mixed` — keyboard value entry breaks in Bitwig, works in REAPER).

Both forum threads are now behind bot challenges — Cloudflare on Gearspace, an
Anubis proof-of-work on LinuxMusicians — so they were read through the Internet
Archive instead. That changed things:

- **Omnisphere goes from `reported, mixed` to `confirmed broken`.** The thread the
  'mixed' reading came from contains no report of it working: one frozen GUI, one
  unconfirmed suggestion to downgrade Wine, and ten posts of argument.
- **Vital's 'reported working bridged' was wrong.** The source lists it under
  *native*. Claim withdrawn.
- **Pianoteq's bridged claim had no URL at all**, so there was nothing to re-open.
  Withdrawn too, and replaced with sources that do open.
- The Gearspace thread turns out to be largely **one tester**, not a community
  consensus. Nothing was promoted on the strength of it. It is a good source
  though — dated, version-specific, and it records failures as well as successes.

Also gained evidence: **Spitfire** (BBC SO hangs Ardour's plugin scan, and has been
moved to JUCE 8 without the vendor saying so) and **Waves** (licence installer
failure, plus a counter-report of it running via iLok machine auth).

Full record — every issue, reporter, date, version, quote, the vendor pages that
would not respond, and the twelve leads left on the table:
[docs/research/2026-08-10-second-sweep.md](docs/research/2026-08-10-second-sweep.md).

Still unresolved: the Reveal Sound site times out from here, so its vendor link is
unverified. Page 2 of the Gearspace thread was not read. And nobody has retested
Omnisphere since February 2025.

## 2026-08-10 — Scope decided: bridged only, native as a note

Considered widening the database to Linux-compatible instruments and effects
generally, native builds included. Decided against it, and wrote the decision down
in three places so it holds: a *Scope* section on the index, a scope block at the
top of `AGENTS.md`, and a "what belongs here" section in `CONTRIBUTING.md`.

Reasoning: the question "does this ship a Linux build?" is answered authoritatively
by the vendor, so the two-independent-sources machinery adds nothing — verification
is only worth doing where nobody official will make the claim. And the cataloguing
is already done: [linuxaudio.org](https://wiki.linuxaudio.org/apps/all) indexes over
1,500 entries, [awesome-linuxaudio](https://github.com/nodiscc/awesome-linuxaudio)
curates plugins and hosts and was last updated 2026-07-31. Both links checked live.

What did get added is the overlap, which was already there informally on the Vital
and Pianoteq pages: a `## Native alternative` section, only for a *same-product*
native build, only on a page that already exists, with the vendor's own wording, a
link and a check date. Explicitly not a place to recommend different plugins that
do a similar job — that is taste, can't be sourced, and never stops growing.

Checked for native builds among the existing rows: **Vital** (Ubuntu 18.04+),
**Pianoteq 9** (Linux listed with Windows, macOS, iOS) and **apulSoft** (apQualizr2
names a Linux 64-bit VST3 host; which other apulSoft plugins are covered isn't clear
from outside, so the page says to check the vendor). **MeldaProduction** and
**Voxengo** were checked and are Wine-only, so they get no section — the rule is
positive claims only, never an assertion that no Linux build exists.

## 2026-08-10 — Verification pass, detail pages, dated entries

Applied the research below to the content, after checking it rather than trusting
it. Every cited yabridge issue was fetched (`gh issue view`) and every brand was
searched against the issue tracker for reports by named users, so each finding now
carries a date, a reporter and a link. The yabridge README and CHANGELOG were read
from the repository at `master`.

Full record — method, every issue and reporter, what stayed unreachable, and the
open questions: [docs/research/2026-08-10-verification.md](docs/research/2026-08-10-verification.md).

Structural change: the README table is now an **index** — plugin, last checked,
status — and each row links to `plugins/<slug>.md` carrying the dated findings,
host DAW, Wine and yabridge versions, fixes and a vendor product link. Version
detail in three columns was the thing making the table unreadable. 31 entries.

`docker/render.py` now renders many sources into `site/` and rewrites links
between them; `docker/check.py` fails the build if a row and its page disagree on
status or date, or if a page lacks a vendor link or findings table. Verified the
image this time: `docker compose up -d --build`, container healthy, index and
detail pages 200, unknown paths 404 (the nginx SPA fallback was removed, it was
serving the index under every wrong URL).

Corrections to the pass below, all from applying the independence rule strictly —
yabridge's README and CHANGELOG are **one** source, not two:

- **TDR Nova** stays `reported`, not `verified`. The only report that could be
  opened is yabridge's own documentation.
- **MeldaProduction** stays `verified`, but on different evidence: independent
  crash reports [#144](https://github.com/robbert-vdh/yabridge/issues/144) and
  [#126](https://github.com/robbert-vdh/yabridge/issues/126), not docs plus a
  Gearspace snippet.
- **Kontakt** `verified` holds, on #372, #356 and #469 from three reporters.
- **Serum** split into Serum 1 (`reported`) and Serum 2 (`confirmed broken`) as
  proposed. #413 and #476 are both Serum 2, from different reporters a year apart.
- **Spitfire Audio** and **Omnisphere** are `reported, mixed` rather than plain
  `reported` — their sources disagree on the outcome. The status vocabulary now
  admits that fourth value, which the UAD row was already using informally.
- **Soundtoys Gullfoss** was dropped: no yabridge issue mentions it and the KVR
  lead could not be opened, so there was nothing to put on a page.
- Gearspace (403) and LinuxMusicians (JS-only) are still unreachable. Rows resting
  on them say "snippet only, thread not opened" on their page.

Host and Wine notes became a second table on the index, as suggested.

## 2026-08-10 — Research pass: yabridge sources

Swept the yabridge repository and community sources for entries missing from the
table and for status changes. Findings below are **not yet applied to the
table** — the snippet-only rows need opening before anything is promoted to
`verified`.

Full record, with every source, the complete upstream known-issues list, the
issue-by-issue notes and the open questions:
[docs/research/2026-08-10-yabridge-sweep.md](docs/research/2026-08-10-yabridge-sweep.md).
The summary below is the reviewable version of it.

Reference points: yabridge master at `b580a9f` (2026-08-02); latest *release* is
still 5.1.1 (2024-12-23), so everything marked "master" below is unreleased.

### Status changes to existing rows

- **Serum** should split. Serum 1 works with fixes (disable `d2d1.dll`, install
  `gdiplus`) per yabridge's known-issues. Serum 2 is broken on stock Wine —
  black GUI, audio fine — partial with Xfer's Wine config keys, working on
  patched Wine.
  [#413](https://github.com/robbert-vdh/yabridge/issues/413) (2025-03-19),
  [#476](https://github.com/robbert-vdh/yabridge/issues/476) (2026-04-27; Bitwig
  6.0, Wine Staging 11.7, yabridge 5.1.1-7),
  [CHANGELOG unreleased](https://github.com/robbert-vdh/yabridge/blob/master/CHANGELOG.md),
  [wine-d2d1-dcomp](https://github.com/mklnln/wine-d2d1-dcomp).
- **Kontakt (NI)** → `verified`. Works; Native Access 2.x needs Wine work (legacy
  1.x installer, Windows 10 mode, manual .iso mount). VST3 patch-load slowness in
  REAPER fixed in 5.0.5 (2023-05-07).
- **MeldaProduction** → `verified`, caveats: disable GPU acceleration; offscreen
  popup positioning fixed on master; CPU higher than on Windows.
- **TDR Nova** → `verified`, caveats: set Continuous Drag to Linear.
- **UAD / Waves / Plugin Alliance** — split **Waves V13 VST3** out as
  `confirmed broken`: memory issues and random crashes, V12 recommended.
- **iZotope** stays `confirmed broken`, now second-sourced (Wine crypt32 auth).

### New entries — verified

- **JUCE 8 plugins needing Direct2D 1.3** — broken: black window and crash, as
  Wine implements D2D to 1.2 and lacks `dcomp.dll`. Named: Audio Modeling SWAM
  and Ambiente, Aberrant DSP, Hertz Drums, Synchro Arts VocAlign 6 Pro. Hosts:
  Bitwig, REAPER, Mixbus. Fixable only by a vendor Wine fallback or patched Wine.
  [#386](https://github.com/robbert-vdh/yabridge/issues/386) (opened 2024-12-18,
  closed 2026-06-04),
  [Wine bug 57833](https://list.winehq.org/hyperkitty/list/wine-bugs@list.winehq.org/message/VINNBRTJCXRSDT4IVS5HZODD753JMBXT/),
  [JUCE forum 64298](https://forum.juce.com/t/juce8-direct2d-wine-yabridge/64298),
  [wine-d2d1-dcomp](https://github.com/mklnln/wine-d2d1-dcomp).
- **Arturia** — works with caveats: tooltip GUI freeze needs winecfg "Hide Wine
  version"; VST3 hitbox/mouse misalignment on Wayland+KDE
  ([#497](https://github.com/robbert-vdh/yabridge/issues/497), 2026-08-06);
  implicated in Bitwig indexing timeouts
  ([#354](https://github.com/robbert-vdh/yabridge/issues/354), 2024-07-16).
- **Minimal Audio Squash** and **apulSoft apUnmask** — work: JUCE 8 but ship a
  Wine-detect software-render fallback. Useful counter-examples to the row above.

### New entries — reported (single source)

From yabridge's known-issues unless noted: Spitfire Audio (BBC SO, LABS — clean
prefix), Sonic Academy Kick 2 and Cytomic The Drop (tooltip freeze), Plogue
Sforzando (redraw only), Voxengo (radial knob mode), Scaler 2 (software
rendering), ujam / Gorilla Engine / Loopcloud (`disable_pipes`), D16 Group
(**broken** — authorization not recalled), Cherry Audio (Bitwig indexing
timeouts, #354), Audio Nebula Aurora FM and PolyChrome DSP McRocklin Suite
(fixed in 5.0.2 / 5.0.5), Pianoteq 9 (works bridged on patched Wine; native build
preferred, same footnote as Vital), Spectrasonics Omnisphere (mixed —
[LinuxMusicians, 2025](https://linuxmusicians.com/viewtopic.php?t=27992)),
Soundtheory Gullfoss (KVR).

### Host and environment notes

Candidates for a second table on the site rather than plugin rows:

- **Wine 9.22 through 11.x do not work with released yabridge 5.1.1** — mouse
  clicks don't register. Downgrade to Wine 9.21 or run a dev build; fixed on
  master.
- **Ubuntu 24.10 + Ardour** — prebuilt binaries hang and consume memory until the
  host crashes; worked around on master. Related:
  [#377](https://github.com/robbert-vdh/yabridge/issues/377) (2024-10-20, also
  Bitwig and Studio One on Kubuntu 24.10).
- **Ardour 7.3–8.1** — some VST3 plugins freeze; 8.2 queries `yabridge_version`
  to fix it (5.1.0).
- **REAPER** — VST3 modules stay loaded without "Allow complete unload of VST
  plug-ins"; drag-and-drop needs `editor_force_dnd`.
  [#472](https://github.com/robbert-vdh/yabridge/issues/472) (GNOME/NVIDIA
  redraw) closed 2026-06-28.
- **Wine 11.12 + KDE Plasma 6** — VST3 editor crashes, open:
  [#488](https://github.com/robbert-vdh/yabridge/issues/488).
- `editor_xembed` and `editor_coordinate_hack` have been removed from yabridge.

### Evidence gaps

- gearspace.com, linuxmusicians.com, kvraudio.com, forum.juce.com, reddit,
  interfacinglinux.com, meow.garden and litui.ca were unreachable from the
  research environment (blocked egress). Claims resting on those are from search
  snippets only and stay `reported` until someone opens the thread.
- Reddit is unreachable both ways, so the r/linuxaudio and r/linux_gaming angle
  is unverified beyond the Native Instruments thread already cited.
- `Valhalla Room` likely has a second source (a Bitwig write-up naming Morph 2,
  Kontakt and Valhalla Room as working) that could not be opened — left at
  `reported`.

## 2026-08-10 — Site pipeline

Converted the hand-written `index.html` into `README.md` plus tooling that
renders it back to a styled page, so the content is editable and reviewable as
markdown and the page is a build artifact.

- `docker/render.py` converts the README, wraps the status column in badge spans
  and rewrites relative links to sibling markdown files so they resolve from the
  published page. `docker/template.html` carries the original dark palette,
  retargeted from hand-written classes to plain elements.
- Two-stage Dockerfile (python render → nginx), `docker-compose.yml` for a host
  port and `docker-compose.traefik.yml` as a subdomain overlay. The overlay
  drops the published port and joins Traefik's network, which needs Compose
  v2.24+ for `!reset`.
- `index.html` is now generated and gitignored — the removed file stays in git
  history if the original markup is ever needed.
- The image build itself is unverified: no Docker daemon was available. Both
  compose configurations were validated with `docker compose config`, and the
  render output was checked by hand.

Docs went to the audience that needs them: `CONTRIBUTING.md` for adding entries,
`docker/README.md` for build and hosting, `AGENTS.md` for agents editing the
table.
