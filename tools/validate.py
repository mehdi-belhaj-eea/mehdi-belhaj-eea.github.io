#!/usr/bin/env python3
# Minimal site validator: HTML parses + every local href/src exists.
import os, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []

class P(HTMLParser):
    def __init__(self, base):
        super().__init__(); self.base = base
    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if k in ("href", "src") and v and not v.startswith(("http", "#", "mailto:", "tel:")):
                path = os.path.normpath(os.path.join(self.base, v.split("#")[0]))
                if v.startswith("/"):
                    path = os.path.normpath(ROOT + v.split("#")[0])
                if v.split("#")[0] and not os.path.exists(path):
                    errors.append(f"missing: {v} (in {self.base})")

for page in ("index.html", "en/index.html", "mentions-legales.html"):
    full = os.path.join(ROOT, page)
    html = open(full, encoding="utf-8").read()
    p = P(os.path.dirname(full)); p.feed(html)
    for must in ("cal.com", "github.com/mehdi-belhaj-eea", "og-card.png"):
        if must not in html and page != "mentions-legales.html":
            errors.append(f"{page}: expected string missing: {must}")

if errors:
    print("\n".join(errors)); sys.exit(1)
print("site OK: 3 pages, all local links resolve")
