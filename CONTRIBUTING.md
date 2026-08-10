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
independent sources — they carry no attribution and cannot be checked.

## How the page is built

`README.md` is the single source of truth. `docker/render.py` converts it to
HTML with [python-markdown](https://pypi.org/project/Markdown/), wraps the
status column in badge spans, and injects the result into
`docker/template.html`. The Dockerfile does that in a build stage and copies the
finished `index.html` into an nginx image.

Render it locally without Docker:

```sh
pip install markdown
python docker/render.py README.md docker/template.html index.html
```

## Serving it

Local run, published on a host port:

```sh
cp .env.example .env
docker compose up -d --build   # http://localhost:8080
```

On a subdomain behind an existing [Traefik](https://traefik.io/), add the
overlay — it drops the host port, joins Traefik's network, and adds the router
labels for `SITE_HOST`:

```sh
cp .env.example .env           # set SITE_HOST=yabridge.example.com
docker compose -f docker-compose.yml -f docker-compose.traefik.yml up -d --build
```

| Variable | Default | Purpose |
| --- | --- | --- |
| `HTTP_PORT` | `8080` | Host port used by `docker-compose.yml` alone |
| `SITE_HOST` | `yabridge.localhost` | Subdomain Traefik routes to the container |
| `TRAEFIK_NETWORK` | `web` | Existing external Docker network Traefik watches |
| `TRAEFIK_CERT_RESOLVER` | `letsencrypt` | Traefik resolver used for TLS |

The overlay expects Traefik to already be running with the Docker provider, a
`websecure` entrypoint, and that certificate resolver. Any other proxy works
too — point it at the published `HTTP_PORT`, or attach the container to your
proxy's network and target port 80.

The page is baked into the image, so re-run the same `up -d --build` after
editing the README.

## Layout

| Path | Role |
| --- | --- |
| `README.md` | Content — the tracker table lives here |
| `CONTRIBUTING.md` | This file — contributor and build documentation |
| `docker/render.py` | Markdown → HTML renderer (adds status badges) |
| `docker/template.html` | Page shell and styling |
| `docker/nginx.conf` | Server config for the runtime image |
| `Dockerfile` | Render stage + nginx stage |
| `docker-compose.yml` | Local/host-port service definition |
| `docker-compose.traefik.yml` | Subdomain overlay for Traefik |
