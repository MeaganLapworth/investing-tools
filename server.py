#!/usr/bin/env python3
"""
Yield Portfolio Tracker — Local Server
Run this script, then open http://localhost:8080 in your browser.
Your API key never leaves your computer.
"""

import http.server
import urllib.request
import urllib.parse
import json
import os
import webbrowser
import threading

# ── Your FMP API key ───────────────────────────────────────────────────────
FMP_API_KEY = "YOUR_API_KEY_HERE"
FMP_BASE    = "https://financialmodelingprep.com/stable"
PORT        = 8080

# ── Server ─────────────────────────────────────────────────────────────────
class Handler(http.server.SimpleHTTPRequestHandler):

    def log_message(self, fmt, *args):
        # Quieter logs
        if "fmp" in args[0] if args else False:
            print(f"  API: {args[0]}")

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)

        # Serve the HTML app at /
        if parsed.path in ('/', '/index.html', '/income-tracker.html'):
            self.serve_file('income-tracker.html', 'text/html')

        # Proxy FMP API calls at /fmp?endpoint=...&symbol=...
        elif parsed.path == '/fmp':
            self.proxy_fmp(parsed.query)

        else:
            self.send_error(404, "Not found")

    def serve_file(self, filename, content_type):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir, filename)
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
            self.send_response(200)
            self.send_header('Content-Type', content_type + '; charset=utf-8')
            self.send_header('Content-Length', len(data))
            self.end_headers()
            self.wfile.write(data)
        except FileNotFoundError:
            self.send_error(404, f"{filename} not found next to server.py")

    def proxy_fmp(self, query_string):
        params = urllib.parse.parse_qs(query_string)
        endpoint = params.get('endpoint', [''])[0]
        if not endpoint:
            self.send_error(400, "Missing endpoint parameter")
            return

        # Build FMP URL — use /stable/ base
        fmp_params = {k: v[0] for k, v in params.items() if k != 'endpoint'}
        fmp_params['apikey'] = FMP_API_KEY
        qs = urllib.parse.urlencode(fmp_params)
        fmp_url = f"{FMP_BASE}/{endpoint}?{qs}"

        print(f"  → {FMP_BASE}/{endpoint}?{qs.replace(FMP_API_KEY, '***')}")

        try:
            req = urllib.request.Request(fmp_url, headers={'User-Agent': 'YieldTracker/1.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                body = resp.read()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(body)
        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8', errors='replace')
            self.send_response(e.code)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(f"FMP error {e.code}: {body}".encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(str(e).encode())


def open_browser():
    import time
    time.sleep(1.0)
    webbrowser.open(f"http://localhost:{PORT}")


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    print("=" * 55)
    print("  Yield Portfolio Tracker — Local Server")
    print("=" * 55)
    print(f"  Address:  http://localhost:{PORT}")
    print(f"  Folder:   {script_dir}")
    print(f"  API key:  ***{FMP_API_KEY[-6:]}")
    print()
    print("  Opening browser automatically...")
    print("  Press Ctrl+C to stop the server.")
    print("=" * 55)

    threading.Thread(target=open_browser, daemon=True).start()

    server = http.server.HTTPServer(('localhost', PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
