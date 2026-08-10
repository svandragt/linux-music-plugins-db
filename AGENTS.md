# AGENTS.md

Instructions for coding agents working in this repository.

## What this repository is

An unofficial compatibility tracker for running Windows audio plugins on Linux
through yabridge. It is a content repository with a small static-site pipeline
attached — the data matters more than the code.

## Rules

- `README.md` is the index: one row per plugin, `| Plugin / brand | Last checked |
  Status |`, the plugin name linking to its page. `plugins/<slug>.md` holds the
  detail. Both are content; edit them, not the output.
- Never edit anything in `site/`. It is generated and gitignored. Regenerate:
  `python3 docker/render.py docker/template.html site README.md plugins/*.md`
  (needs `pip install markdown`).
- Run `python3 docker/check.py` after any content change. It fails if a row and
  its page disagree on status or date, if either side is missing, or if a page
  has no vendor link or findings table.
- Status must be one of `verified`, `reported`, `confirmed broken`,
  `reported, mixed` — the renderer colours the badge by matching that text, so
  don't invent new values without updating `STATUS_CLASSES` in `docker/render.py`
  and `VALID` in `docker/check.py`.
- Every plugin page needs: the status line
  (`*Status: <status> · last checked <YYYY-MM-DD>*`), a `[Vendor page](...)` link
  to the product, and a `## Findings` table where every row carries a date and a
  link to the source.

## Evidence rules

- `verified` means two or more independent sources. One source is `reported`.
  yabridge's README and CHANGELOG count as **one** source between them — they are
  one project's voice. Separate GitHub issues from different reporters are
  independent. Vendor testimonials are not sources.
- Read the source before citing it. A search-engine snippet is a lead, not
  evidence — say so on the page ("snippet only, thread not opened") and leave the
  entry at `reported`.
- Record what the report actually covers: plugin, vendor, host DAW, method
  (yabridge / native / plain Wine), and outcome. A plugin that works in Bitwig
  and breaks in Ardour is one page with a caveat, not two entries.
- Note when a claim is version-bound. Wine and yabridge versions move fast and
  status changes with them; a fix landing on yabridge `master` is not the same as
  a released fix.
- Report status *changes* to existing entries as well as new plugins — a
  previously broken plugin that now works is the most useful thing this database
  can say.
- Don't promote an entry to `verified` on the strength of two reports that trace
  back to the same person or thread.
- Add a [JOURNAL.md](JOURNAL.md) entry, newest first, after a research pass or a
  change to the pipeline. Record what was checked, what was decided, and what is
  still unresolved — including sources you could not open. A single-row fix needs
  no entry; the commit message covers it.
- Commit the full evidence from a research pass to `docs/research/<date>-<topic>.md`
  and link it from the journal entry. Every claim, every URL, every date, every
  version, and every source you could not reach — including leads too weak for
  the table. Losing the raw findings costs more than the file does; the journal
  entry is the summary, not the record.

## Build and hosting

See [docker/README.md](docker/README.md).
