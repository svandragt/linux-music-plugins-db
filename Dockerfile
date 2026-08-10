# Stage 1: render README.md -> index.html
FROM python:3.12-alpine AS render

RUN pip install --no-cache-dir "markdown==3.6"

WORKDIR /build
COPY docker/render.py docker/template.html ./docker/
COPY README.md ./
RUN python docker/render.py README.md docker/template.html index.html

# Stage 2: serve it
FROM nginx:1.27-alpine

COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=render /build/index.html /usr/share/nginx/html/index.html

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD wget -qO /dev/null http://127.0.0.1/ || exit 1
