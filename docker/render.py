#!/usr/bin/env python3
"""Render README.md into a static index.html using an HTML template.

Usage: render.py <source.md> <template.html> <output.html>

The template must contain the placeholders {{TITLE}} and {{CONTENT}}. Links to
sibling markdown files (CONTRIBUTING.md and such) are rewritten to point at the
repository, since those files are not published alongside the page.
"""

import html
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


def link_markdown_files(html_text):
    """Point relative links to .md files at the repository instead of the site."""
    return re.sub(
        r'href="(?!\w+:|//|#)([^"]+\.md)"',
        rf'href="{REPO_URL}/blob/main/\1"',
        html_text,
    )


def extract_title(source):
    match = re.search(r"^#\s+(.+)$", source, flags=re.MULTILINE)
    return match.group(1).strip() if match else "README"


def main(argv):
    if len(argv) != 4:
        sys.exit(__doc__.strip())

    source_path, template_path, output_path = argv[1:]

    with open(source_path, encoding="utf-8") as fh:
        source = fh.read()

    title = extract_title(source)

    body = markdown.markdown(source, extensions=["tables", "sane_lists"])
    body = tagify(badgeify(link_markdown_files(body)))
    body = "\n".join("    " + line for line in body.splitlines())

    with open(template_path, encoding="utf-8") as fh:
        page = fh.read()

    page = page.replace("{{TITLE}}", html.escape(title)).replace("{{CONTENT}}", body)

    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(page)

    print(f"wrote {output_path} ({len(page)} bytes)")


if __name__ == "__main__":
    main(sys.argv)
