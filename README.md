# yabridge compatibility tracker

*unofficial · crowd-sourced · not affiliated with yabridge*

There's no ProtonDB for yabridge. This is a manually compiled read of what's
floating around forums, the yabridge GitHub, and vendor claims — cross-checked
for how many independent sources actually back each entry.

## Legend

- **verified** — 2+ independent sources
- **reported** — single source only
- **confirmed broken** — does not work

## Plugins

| Plugin / brand | Reported by | Status |
| --- | --- | --- |
| FabFilter suite | Gearspace forum, yabridge GitHub known-issues, yabridge.org testimonials | verified |
| Neural DSP (Darkglass etc.) | Gearspace forum, yabridge CHANGELOG (freeze fix) | verified |
| Kontakt (Native Instruments) | yabridge.org testimonial | reported |
| Serum (Xfer Records) | yabridge.org testimonial | reported |
| KiloHearts plugins | yabridge GitHub known-issues (esync/fsync fix) | reported |
| Brainworx plugins | Gearspace forum | reported |
| Valhalla Room | Gearspace forum | reported |
| Klanghelm | Gearspace forum | reported |
| TDR Nova | Gearspace forum | reported |
| MeldaProduction | Gearspace forum | reported |
| Applied Acoustics (Chromaphone 3) | yabridge GitHub known-issues (hide_daw fix, Bitwig only) | reported |
| Soundtoys / PSPaudioware | yabridge GitHub known-issues (GUI position fix) | reported |
| UAD / Waves / Plugin Alliance | Gearspace forum — got working, then abandoned for stability | reported, mixed |
| Vital | Gearspace forum (native Linux build exists anyway) | reported |
| iZotope plugins | yabridge GitHub known-issues — auth fails, missing Wine crypt32 support | confirmed broken |

## Contributing

Edit the table above and open a pull request. Please include the source you're
citing — a forum thread, a GitHub issue, or a CHANGELOG entry. An entry moves
from *reported* to *verified* once two independent sources back it. See
[CONTRIBUTING.md](CONTRIBUTING.md) for how the page is built and served.

## Sources

- [yabridge GitHub — known issues & fixes](https://github.com/robbert-vdh/yabridge)
- [Gearspace: Linux-compatible hardware/software/plugins](https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html)
- yabridge.org testimonials (unverifiable, treat as marketing)

No centralized compatibility database exists for yabridge — this list is
anecdotal and will drift out of date as Wine and plugin versions change.
