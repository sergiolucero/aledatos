"""Serve valpo1.html and proxy CARTO tiles using CARTODB_API_KEY.

Run: python server.py
Open: http://127.0.0.1:8000
The configured key is forwarded server-side using CARTO's `key` parameter
and is never included in the HTML or browser requests.
"""

import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen


PAGE = Path(__file__).with_name("valpo1.html")
TILE_PATH = re.compile(r"/carto-tiles/voyager/(\d{1,2})/(\d+)/(\d+)(@2x)?\.png")


def load_api_key():
    key = os.environ.get("CARTODB_API_KEY", "").strip()
    if not key and os.name == "nt":
        # Also support a saved Windows user variable in an already-open terminal.
        import winreg
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as env:
                key = winreg.QueryValueEx(env, "CARTODB_API_KEY")[0].strip()
        except OSError:
            pass
    if not key:
        raise SystemExit("Set CARTODB_API_KEY before starting this server.")
    return key


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlsplit(self.path).path
        if path in ("/", "/valpo1.html"):
            self.respond(PAGE.read_bytes(), "text/html; charset=utf-8", "no-store")
            return

        match = TILE_PATH.fullmatch(path)
        if not match:
            self.send_error(404)
            return
        z, x, y = map(int, match.group(1, 2, 3))
        if not (0 <= z <= 20 and 0 <= x < 2**z and 0 <= y < 2**z):
            self.send_error(400, "Invalid tile coordinates")
            return
        retina = match.group(4) or ""
        query = urlencode({"key": self.server.api_key})
        url = f"https://basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{retina}.png?{query}"
        try:
            request = Request(url, headers={"User-Agent": "ValpoMaps/1.0"})
            with urlopen(request, timeout=20) as response:
                self.respond(response.read(), "image/png", "private, max-age=3600")
        except (HTTPError, URLError, TimeoutError, OSError):
            # Never return upstream URLs or exception details containing the key.
            self.send_error(502, "Unable to load CARTO tile")

    def respond(self, body, content_type, cache_control):
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", cache_control)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    key = load_api_key()
    with ThreadingHTTPServer(("127.0.0.1", 8000), Handler) as server:
        server.api_key = key
        print("ValpoMaps: http://127.0.0.1:8000 (Ctrl+C to stop)", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
