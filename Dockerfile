# Stage 1: render the markdown sources -> site/
FROM python:3.14-alpine AS render

RUN pip install --no-cache-dir "markdown==3.6"

WORKDIR /build
COPY docker/render.py docker/check.py docker/template.html ./docker/
COPY README.md ./
COPY plugins ./plugins/
RUN python docker/check.py \
 && python docker/render.py docker/template.html site README.md plugins/*.md

# Stage 2: serve it
FROM nginx:1.27-alpine

COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=render /build/site/ /usr/share/nginx/html/

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD wget -qO /dev/null http://127.0.0.1/ || exit 1
