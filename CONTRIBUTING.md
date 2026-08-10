# Contributing

## How the content is arranged

[README.md](README.md) holds the index table: one row per plugin, its status, and
the date it was last checked. The detail lives in `plugins/<slug>.md` — one page
per row, holding the dated reports, the host DAW and Wine or yabridge versions,
the fixes needed, and a link to the vendor's product page.

Both files are the content. `site/` is generated output, so never edit it.

## Adding or changing an entry

1. Add or edit `plugins/<slug>.md`. Copy the shape of an existing page: the
   status line, the vendor link, a short summary, caveats, and a findings table.
2. Add or update the row in the README table. The status and the last-checked
   date must match the page's status line — `python3 docker/check.py` fails if
   they drift.
3. Open a pull request.

Status values:

| Status | Meaning |
| --- | --- |
| `verified` | 2+ independent sources |
| `reported` | single source only |
| `confirmed broken` | does not work |
| `reported, mixed` | sources disagree on the outcome |

A source is a report you can open and read. yabridge's README and CHANGELOG
count as one source between them — they are one project's voice, so a claim
resting only on them is `reported`, not `verified`. Vendor testimonials (for
example the quotes on yabridge.org) are not sources: they carry no attribution
and cannot be checked. A search engine snippet is a lead, not a source — open the
thread and cite the post, and say so on the page when you couldn't.

Every findings row needs a date. Use the date the report was made, and use the
date you checked for anything drawn from documentation that carries no date.

## Previewing your change

```sh
pip install markdown
python3 docker/check.py
python3 docker/render.py docker/template.html site README.md plugins/*.md
```

Open `site/index.html` in a browser. Check that new rows picked up the right
status badge — the renderer colours the last column by its text.

Build and hosting details live in [docker/README.md](docker/README.md).
