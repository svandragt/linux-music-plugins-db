# Build and hosting

`README.md` and `plugins/*.md` in the repository are the single source of truth.
`render.py` converts each of them to HTML with
[python-markdown](https://pypi.org/project/Markdown/), wraps the status column in
badge spans, rewrites links between the rendered pages to their `.html` output
(and links to unpublished markdown files to the repository), and injects the
result into `template.html`. `README.md` becomes `index.html`; the plugin pages
keep their path, so `plugins/serum-2.md` is served at `/plugins/serum-2.html`.

The Dockerfile runs `check.py` first — a build fails rather than publishing an
index that disagrees with its own detail pages — then renders into `site/` and
copies that tree into an nginx image.

Render locally with:

```sh
python3 docker/check.py
python3 docker/render.py docker/template.html site README.md plugins/*.md
```

## Run it locally

```sh
cp .env.example .env
docker compose up -d --build   # http://localhost:8080
```

## Serve it on a subdomain

Behind an existing [Traefik](https://traefik.io/), add the overlay — it drops
the host port, joins Traefik's network, and adds the router labels for
`SITE_HOST`:

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
`websecure` entrypoint, and that certificate resolver, and needs Compose v2.24+
for the `!reset` tag. Any other proxy works too — point it at the published
`HTTP_PORT`, or attach the container to your proxy's network and target port 80.

The pages are baked into the image, so re-run the same `up -d --build` after
editing any markdown.

## Layout

| Path | Role |
| --- | --- |
| `README.md` | Content — the index table lives here |
| `plugins/*.md` | Content — one detail page per tracked plugin |
| `CONTRIBUTING.md` | How to add or change an entry |
| `AGENTS.md` | Instructions for coding agents working in this repository |
| `JOURNAL.md` | Dated research passes and pipeline changes |
| `docs/research/` | Full evidence behind each research pass |
| `docker/README.md` | This file — build and hosting |
| `docker/render.py` | Markdown → HTML renderer (adds status badges) |
| `docker/check.py` | Fails if the index and the plugin pages disagree |
| `docker/template.html` | Page shell and styling |
| `docker/nginx.conf` | Server config for the runtime image |
| `Dockerfile` | Render stage + nginx stage |
| `docker-compose.yml` | Local/host-port service definition |
| `docker-compose.traefik.yml` | Subdomain overlay for Traefik |
