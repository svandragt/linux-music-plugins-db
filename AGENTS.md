# AGENTS.md

Instructions for coding agents working in this repository.

## What this repository is

An unofficial compatibility tracker for running Windows audio plugins on Linux
through yabridge. It is a content repository with a small static-site pipeline
attached — the data matters more than the code.

## Rules

- `README.md` holds the content. Edit the table there; it is what the site shows.
- Never edit `index.html`. It is generated and gitignored. Regenerate instead:
  `python docker/render.py README.md docker/template.html index.html`
  (needs `pip install markdown`).
- Keep the table's three columns: *Plugin / brand*, *Reported by*, *Status*.
  Status must be one of `verified`, `reported`, `confirmed broken` — the
  renderer colours the badge by matching that text, so don't invent new values
  without updating `STATUS_CLASSES` in `docker/render.py`.
- `verified` means two or more independent sources. One source is `reported`.
  Vendor testimonials (yabridge.org quotes and similar) are not sources.
- Cite something checkable in the *Reported by* column: a forum thread, a GitHub
  issue number, a CHANGELOG entry. Prefer a link over a name.

## When researching new entries

- Read the source before citing it. A search-engine snippet is a lead, not
  evidence — say so plainly if a claim rests only on a snippet, and leave the
  entry at `reported`.
- Record what the report actually covers: plugin, vendor, host DAW, method
  (yabridge / native / plain Wine), and outcome. A plugin that works in Bitwig
  and breaks in Ardour is one entry with a caveat, not two entries.
- Note when a claim is version-bound. Wine and yabridge versions move fast and
  status changes with them; a fix landing on yabridge `master` is not the same as
  a released fix.
- Report status *changes* to existing rows as well as new plugins — a previously
  broken plugin that now works is the most useful thing this database can say.
- Don't promote an entry to `verified` on the strength of two reports that trace
  back to the same person or thread.

- Add a [JOURNAL.md](JOURNAL.md) entry, newest first, after a research pass or a
  change to the pipeline. Record what was checked, what was decided, and what is
  still unresolved — including sources you could not open. A single-row fix needs
  no entry; the commit message covers it.

## Build and hosting

See [docker/README.md](docker/README.md). Verify a change by rendering the page
locally; `docker build` needs a Docker daemon, which is not always available.
