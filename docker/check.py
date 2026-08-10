#!/usr/bin/env python3
"""Check the index table against the plugin pages. Run: python3 docker/check.py

Fails if a row and its page disagree, if either side has an entry the other
doesn't, or if a page is missing its status line, vendor link or findings table.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROW = re.compile(r"^\|\s*\[[^\]]+\]\(plugins/([\w.-]+)\.md\)\s*\|([^|]*)\|([^|]*)\|")
STATUS = re.compile(r"^\*Status:\s*(.+?)\s*·\s*last checked\s*(\d{4}-\d\d-\d\d)\s*\*$")
VALID = {"verified", "reported", "confirmed broken", "reported, mixed"}


def read(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as fh:
        return fh.read()


def index_rows():
    rows = {}
    for line in read("README.md").splitlines():
        match = ROW.match(line)
        if match:
            slug, checked, status = match.groups()
            rows[slug] = (checked.strip(), status.strip())
    return rows


def page_facts(slug):
    text = read("plugins", f"{slug}.md")
    status_line = next(
        (m for m in (STATUS.match(l) for l in text.splitlines()) if m), None
    )
    return status_line, text


def main():
    errors = []
    rows = index_rows()
    files = {
        f[:-3] for f in os.listdir(os.path.join(ROOT, "plugins")) if f.endswith(".md")
    }

    for slug in sorted(files - rows.keys()):
        errors.append(f"plugins/{slug}.md has no row in README.md")
    for slug in sorted(rows.keys() - files):
        errors.append(f"README.md links plugins/{slug}.md, which does not exist")

    for slug in sorted(rows.keys() & files):
        row_checked, row_status = rows[slug]
        status_line, text = page_facts(slug)
        if not status_line:
            errors.append(f"plugins/{slug}.md: no '*Status: ... · last checked ...*'")
            continue
        page_status, page_checked = status_line.group(1), status_line.group(2)
        if page_status != row_status:
            errors.append(
                f"{slug}: status '{row_status}' in README, '{page_status}' on page"
            )
        if page_checked != row_checked:
            errors.append(
                f"{slug}: last checked {row_checked} in README, {page_checked} on page"
            )
        if row_status not in VALID:
            errors.append(f"{slug}: unknown status '{row_status}'")
        if "[Vendor page](http" not in text:
            errors.append(f"plugins/{slug}.md: no vendor page link")
        if "## Findings" not in text or "| Date |" not in text:
            errors.append(f"plugins/{slug}.md: no findings table")

    for error in errors:
        print(error)
    print(f"{len(rows)} entries, {len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
