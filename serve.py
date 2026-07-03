#!/usr/bin/env python3
"""Tiny static dev server that disables caching.

Why: the stock `python3 -m http.server` lets the browser cache CSS/JS, so
edits don't show up without a hard refresh. This sends no-store on every
response so the site always reflects the latest files during development.

Usage:
  python3 serve.py [port] [directory]
    port      - default 8080
    directory - folder to serve; default is the current directory. Lets the
                umbrella run it against this site's subfolder.
"""
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    if len(sys.argv) > 2:
        os.chdir(sys.argv[2])
    print(f"Serving Ari's Mobile Detailing (no-cache) from {os.getcwd()} at http://localhost:{port}")
    HTTPServer(("127.0.0.1", port), NoCacheHandler).serve_forever()
