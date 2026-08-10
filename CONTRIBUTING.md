# Contributing

## Adding or changing an entry

The tracker table in [README.md](README.md) is the content — edit it there and
open a pull request. `index.html` is generated, so never edit it by hand.

Include the source you're citing in the *Reported by* column: a forum thread, a
GitHub issue, or a CHANGELOG entry. Status values are:

| Status | Meaning |
| --- | --- |
| `verified` | 2+ independent sources |
| `reported` | single source only |
| `confirmed broken` | does not work |

An entry moves from `reported` to `verified` once a second independent source
backs it. Vendor testimonials (for example the quotes on yabridge.org) are not
independent sources — they carry no attribution and cannot be checked. A search
engine snippet is a lead, not a source: open the thread and cite the post.

## Previewing your change

The site is rendered from the README, so a preview is one command:

```sh
pip install markdown
python docker/render.py README.md docker/template.html index.html
```

Open `index.html` in a browser. Check that new rows picked up the right status
badge — the renderer colours the last column by its text.

Build and hosting details live in [docker/README.md](docker/README.md).
