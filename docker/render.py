#!/usr/bin/env python3
"""Render markdown sources into static HTML pages using a shared template.

Usage: render.py <template.html> <output-dir> <source.md>...

`README.md` becomes `index.html`; any other source keeps its relative path with
an `.html` extension, so `plugins/serum-2.md` becomes `plugins/serum-2.html`.
The template must contain the placeholders {{TITLE}} and {{CONTENT}}.

Relative links between rendered sources are rewritten to their `.html` output.
Links to markdown files that are not being rendered (CONTRIBUTING.md and such)
point at the repository instead, since those files are not published.
"""

import html
import os
import posixpath
import re
import sys

import markdown

REPO_URL = "https://github.com/svandragt/linux-music-plugins-db"

# Status text in the last table column -> badge/dot modifier class.
STATUS_CLASSES = (
    ("broken", "broken"),
    ("verified", "yes"),
)


def status_class(text):
    lowered = text.lower()
    for needle, cls in STATUS_CLASSES:
        if needle in lowered:
            return cls
    return "no"


def badgeify(html_text):
    """Wrap the status cell of each table row in a badge span."""

    def repl(match):
        cell = match.group(1).strip()
        if not cell or "<" in cell:
            return match.group(0)
        cls = status_class(cell)
        return (
            f'<td><span class="badge {cls}">'
            f'<i class="dot {cls}"></i>{cell}</span></td>'
        )

    # Only the final cell of a row carries a status.
    return re.sub(r"<td>([^<]*)</td>\s*(?=</tr>)", repl, html_text)


def tagify(html_text):
    """Give the first italic-only paragraph the .tag class (the strapline)."""
    return re.sub(
        r"<p>(<em>.*?</em>)</p>",
        r'<p class="tag">\1</p>',
        html_text,
        count=1,
        flags=re.DOTALL,
    )


def output_path(source):
    """Relative output path for a source: README.md -> index.html."""
    source = source.replace(os.sep, "/")
    if source == "README.md":
        return "index.html"
    return re.sub(r"\.md$", ".html", source)


def link_markdown_files(html_text, page, pages):
    """Rewrite relative .md links: to a sibling page, or to the repository.

    `page` is the source path being rendered and `pages` maps every source path
    in this run to its output path, so a link is only rewritten to `.html` when
    the target is actually published.
    """
    page_dir = posixpath.dirname(page.replace(os.sep, "/"))

    def repl(match):
        target = match.group(1)
        resolved = posixpath.normpath(posixpath.join(page_dir, target))
        if resolved in pages:
            href = posixpath.relpath(pages[resolved], page_dir or ".")
        else:
            href = f"{REPO_URL}/blob/main/{resolved}"
        return f'href="{href}"'

    return re.sub(r'href="(?!\w+:|//|#)([^"]+\.md)"', repl, html_text)


def extract_title(source):
    match = re.search(r"^#\s+(.+)$", source, flags=re.MULTILINE)
    return match.group(1).strip() if match else "README"


def render(source_path, template, pages):
    with open(source_path, encoding="utf-8") as fh:
        source = fh.read()

    body = markdown.markdown(source, extensions=["tables", "sane_lists"])
    body = tagify(badgeify(link_markdown_files(body, source_path, pages)))
    body = "\n".join("    " + line for line in body.splitlines())

    title = extract_title(source)
    return template.replace("{{TITLE}}", html.escape(title)).replace(
        "{{CONTENT}}", body
    )


def main(argv):
    if len(argv) < 4:
        sys.exit(__doc__.strip())

    template_path, output_dir = argv[1:3]
    sources = argv[3:]

    with open(template_path, encoding="utf-8") as fh:
        template = fh.read()

    pages = {s.replace(os.sep, "/"): output_path(s) for s in sources}

    for source_path in sources:
        target = os.path.join(output_dir, output_path(source_path))
        os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
        page = render(source_path, template, pages)
        with open(target, "w", encoding="utf-8") as fh:
            fh.write(page)
        print(f"wrote {target} ({len(page)} bytes)")


if __name__ == "__main__":
    main(sys.argv)
