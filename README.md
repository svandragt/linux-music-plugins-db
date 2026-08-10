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
from *reported* to *verified* once two independent sources back it.

## Sources

- [yabridge GitHub — known issues & fixes](https://github.com/robbert-vdh/yabridge)
- [Gearspace: Linux-compatible hardware/software/plugins](https://gearspace.com/board/music-computers/1449241-linux-compatible-hardware-software-plugins.html)
- yabridge.org testimonials (unverifiable, treat as marketing)

No centralized compatibility database exists for yabridge — this list is
anecdotal and will drift out of date as Wine and plugin versions change.

<!-- site:end -->

## Serving this as a website

This README is the single source of truth. The Docker tooling renders it to
`index.html` at image build time and serves it with nginx, so a subdomain such
as `yabridge.example.com` shows the same table as a styled page. Everything
below the `<!-- site:end -->` marker is repository-only and never reaches the
page.

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
editing this README. To render `index.html` locally without Docker:

```sh
pip install markdown
python docker/render.py README.md docker/template.html index.html
```

### Layout

| Path | Role |
| --- | --- |
| `README.md` | Content — the tracker table lives here |
| `docker/render.py` | Markdown → HTML renderer (adds status badges) |
| `docker/template.html` | Page shell and styling |
| `docker/nginx.conf` | Server config for the runtime image |
| `Dockerfile` | Render stage + nginx stage |
| `docker-compose.yml` | Local/host-port service definition |
| `docker-compose.traefik.yml` | Subdomain overlay for Traefik |
