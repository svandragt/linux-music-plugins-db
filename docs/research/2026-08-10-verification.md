# 2026-08-10 — Verification of the yabridge sweep

Raw evidence for the verification pass. The
[journal entry](../../JOURNAL.md) is the summary; this is the record. Companion to
[2026-08-10-yabridge-sweep.md](2026-08-10-yabridge-sweep.md), which is the sweep
being verified here.

## Method

- Every issue cited in the sweep was fetched with
  `gh issue view <n> -R robbert-vdh/yabridge` to confirm the number, state, dates
  and title, rather than trusting the citation.
- Every brand in the table was searched with
  `gh search issues --repo robbert-vdh/yabridge <brand>` to find reports by named
  users, so each finding could carry a date and a reporter.
- `README.md` and `CHANGELOG.md` were read from the repository at `master` via
  `gh api repos/robbert-vdh/yabridge/contents/...`, not from a rendered page.
- Vendor URLs were checked with `curl` for a live response before being linked.

## Cited issues, all confirmed

| Issue | State | Opened | Closed | Title |
| --- | --- | --- | --- | --- |
| [#413](https://github.com/robbert-vdh/yabridge/issues/413) | open | 2025-03-19 | — | Serum 2 graphical issues |
| [#476](https://github.com/robbert-vdh/yabridge/issues/476) | open | 2026-04-27 | — | Serum 2 No GUI |
| [#386](https://github.com/robbert-vdh/yabridge/issues/386) | closed | 2024-12-18 | 2026-06-04 | JUCE8 Plugins Don't Work Causing Black Screen and Crash |
| [#497](https://github.com/robbert-vdh/yabridge/issues/497) | open | 2026-08-06 | — | Arturia VST3 GUI & hitbox / mouse misalignment on Wayland/KDE |
| [#354](https://github.com/robbert-vdh/yabridge/issues/354) | closed | 2024-07-16 | 2024-07-18 | bitwig stopped loading yabridge plugins |
| [#377](https://github.com/robbert-vdh/yabridge/issues/377) | closed | 2024-10-20 | 2024-12-07 | Yabridge doesn't work in Kubuntu 24.10 in Ardour, Bitwig Studio and Presonus Studio One |
| [#472](https://github.com/robbert-vdh/yabridge/issues/472) | closed | 2026-04-06 | 2026-06-28 | REAPER stops redrawing its UI on GNOME / NVIDIA |
| [#488](https://github.com/robbert-vdh/yabridge/issues/488) | open | 2026-07-09 | — | VST3 editor crashes on close with Wine 11.12 on KDE Plasma 6 Wayland |

Every number, state and date in the sweep held up. One nuance: the sweep cites
#413 and #476 for the Serum split, and **both are Serum 2** — the Serum 1 half of
that split rests only on yabridge's known-issues section.

## Independence rule as applied

`verified` needs two sources that are not the same voice.

- yabridge's `README.md` and `CHANGELOG.md` are **one** source between them. Both
  are the maintainer writing about their own project. The sweep treated them as
  two, which is what inflated some statuses.
- Separate issues from different reporters are independent.
- A search-engine snippet is not a source. Where a row rests on one, its page says
  "snippet only, thread not opened".

Consequences: TDR Nova back to `reported`; MeldaProduction stays `verified` but on
#144 and #126 rather than docs plus a snippet; Aurora FM / McRocklin Suite is
`reported` because the CHANGELOG is its only voice; a fourth status value,
`reported, mixed`, for entries whose sources disagree.

## Reports found per brand

Issues used as evidence on the plugin pages, with the reporter as recorded on
GitHub. Claims are kept at the level the title supports — none of these threads
were read line by line.

| Entry | Issues used |
| --- | --- |
| FabFilter | #364 (sidoka-contact, 2024-08-28) |
| Neural DSP | #432 (idealemu, 2025-06-01) |
| Kontakt | #372 (sidoka-contact, 2024-09-30), #356 (RichardJECooke, 2024-07-20), #469 (kernelPanic0x, 2026-03-09) |
| Serum 2 | #413 (drac-dot-gay, 2025-03-19), #476 (smallghostbigthot, 2026-04-27) |
| KiloHearts | #417 (10kmotorola, 2025-04-13), #210 (2022-11-03) |
| MeldaProduction | #144 (JonathanTroyer, 2021-11-03), #126 (SquidRoe, 2021-08-05) |
| Chromaphone 3 | #137 (jonaspeter, 2021-09-17) |
| Soundtoys / PSP | #192 (khughitt, 2022-07-20), #226 (ferorborja, 2022-12-24), #99 (durutti, 2021-04-29), #27 (lentferj, 2020-07-19) |
| Waves V13 VST3 | #402 (pheerai, 2025-02-15), #478 (geextahslex, 2026-04-30) |
| iZotope | #439 (durutti, 2025-06-30) |
| JUCE 8 / Direct2D | #386 (relaborn, 2024-12-18), #467 (sclewis900, 2026-02-25) |
| Arturia | #497 (Leadsingerman0503, 2026-08-06), #468 (duck-117, 2026-02-25), #473 (illegitimate-egg, 2026-04-08) |
| Spitfire Audio | #467 (sclewis900, 2026-02-25) |
| Sforzando | #327 (jbmestelan, 2024-04-02) |
| Voxengo | #388 (cdunford, 2024-12-22) |
| ujam / Gorilla Engine | #205 (Tabinol, 2022-10-10), #47 (plaimbock, 2020-10-23), #163 (TheGuyWhoo, 2022-02-16) |
| D16 Group | #248 (franticnick, 2023-05-07) |
| Cherry Audio | #354 (2024-07-16) |
| Omnisphere | #220 (mukundasik, 2022-12-01) |

Brands with **no** matching issue report, left on documentation or forum snippets
alone: Brainworx / Plugin Alliance, Valhalla Room, Klanghelm, TDR Nova, Scaler 2,
Kick 2 / The Drop, Vital, Pianoteq, UAD, Serum 1, Aurora FM / McRocklin.

## Dropped

- **Soundtheory Gullfoss.** No yabridge issue mentions it and the KVR lead could
  not be opened. Nothing to put on a page, so no row. Re-add it if someone opens
  the KVR thread.

## Sources that stayed unreachable

- `gearspace.com` — HTTP 403 to an automated fetch. Every row resting on the
  Gearspace thread is still snippet-only: FabFilter's third source, Brainworx,
  Valhalla Room, Klanghelm, UAD, Vital.
- `linuxmusicians.com` — serves a JavaScript shell, no content to an automated
  fetch. Affects the Omnisphere mixed reading.
- `kvraudio.com`, `forum.juce.com`, `reddit.com`, `interfacinglinux.com` — not
  retried this pass; the JUCE forum thread is cited from the sweep, not read here.
- Vendor URLs returning 403 to `curl` (Cloudflare, not dead): Native Instruments,
  Valhalla DSP, Minimal Audio, Scaler, Plogue, Sonic Academy. Linked anyway; they
  load in a browser.

## Open questions

- Does the Gearspace thread actually name Klanghelm, Valhalla Room and Brainworx,
  or is that the search snippet paraphrasing? Unresolvable without opening it.
- Is Spitfire's BBC SO black screen the JUCE 8 Direct2D problem rather than a
  Spitfire problem? #467 pairs it with Superior Drummer 3 dropdowns, which suggests
  a shared cause. If so, Spitfire's `reported, mixed` becomes plain `reported` plus
  a cross-reference.
- FabFilter is `verified` partly on #364, a crash report. A crash report proves
  people run it, which is weaker than a report that it works. Worth a second look
  when a clearer source turns up.
