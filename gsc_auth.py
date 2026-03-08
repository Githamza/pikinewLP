#!/usr/bin/env python3
"""Google Search Console OAuth + Data Fetch Script"""

import http.server
import json
import threading
import urllib.parse
import urllib.request
import webbrowser
import os
import sys
import time

CLIENT_ID = os.environ.get("GSC_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("GSC_CLIENT_SECRET", "")
REDIRECT_URI = "http://localhost:8085"
SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"

auth_code = None


class OAuthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        if "code" in params:
            auth_code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><body><h1>Authorization successful!</h1><p>You can close this tab and go back to the terminal.</p></body></html>")
        else:
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            error = params.get("error", ["unknown"])[0]
            self.wfile.write(f"<h1>Error: {error}</h1>".encode())

    def log_message(self, format, *args):
        pass


def get_access_token(code):
    data = urllib.parse.urlencode({
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }).encode()
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"Token exchange error: {e.read().decode()}")
        sys.exit(1)


def gsc_request(access_token, endpoint, method="GET", body=None):
    url = f"https://www.googleapis.com/webmasters/v3/{endpoint}"
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"Bearer {access_token}")
    req.add_header("Content-Type", "application/json")
    if body:
        req.data = json.dumps(body).encode()
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def main():
    # Start local server to catch the OAuth callback
    server = http.server.HTTPServer(("127.0.0.1", 8085), OAuthHandler)
    server.timeout = 300  # 5 minute timeout

    print("Starting local OAuth server on port 8085...")
    print("", flush=True)

    # Open browser
    auth_url = (
        f"https://accounts.google.com/o/oauth2/v2/auth?"
        f"client_id={CLIENT_ID}"
        f"&redirect_uri={urllib.parse.quote(REDIRECT_URI)}"
        f"&scope={urllib.parse.quote(SCOPE)}"
        f"&response_type=code"
        f"&access_type=offline"
        f"&prompt=consent"
    )
    print("Opening browser for authorization...", flush=True)
    print(f"\nIf browser doesn't open, visit this URL:\n{auth_url}\n", flush=True)
    webbrowser.open(auth_url)

    print("Waiting for authorization (up to 5 minutes)...", flush=True)

    # Handle requests until we get the code or timeout
    start = time.time()
    while auth_code is None and (time.time() - start) < 300:
        server.handle_request()

    server.server_close()

    if not auth_code:
        print("ERROR: No authorization code received. Timed out or denied.")
        sys.exit(1)

    print("Got authorization code! Exchanging for token...", flush=True)
    token_data = get_access_token(auth_code)
    access_token = token_data["access_token"]
    print("Access token obtained!\n", flush=True)

    # List sites
    print("=" * 60)
    print("SITES IN YOUR SEARCH CONSOLE")
    print("=" * 60)
    sites = gsc_request(access_token, "sites")
    for site in sites.get("siteEntry", []):
        print(f"  {site['siteUrl']} (permission: {site['permissionLevel']})")

    if not sites.get("siteEntry"):
        print("  No sites found!")
        sys.exit(0)

    all_site_data = []
    for site in sites.get("siteEntry", []):
        site_url = site["siteUrl"]
        site_data = {"url": site_url, "permission": site["permissionLevel"]}
        print(f"\n{'=' * 60}")
        print(f"SEARCH ANALYTICS: {site_url}")
        print(f"{'=' * 60}")

        encoded_site = urllib.parse.quote(site_url, safe='')

        # Overall performance
        body = {
            "startDate": "2026-01-26",
            "endDate": "2026-02-22",
            "dimensions": [],
            "rowLimit": 1,
        }
        try:
            data = gsc_request(access_token, f"sites/{encoded_site}/searchAnalytics/query", method="POST", body=body)
            if data.get("rows"):
                row = data["rows"][0]
                print(f"\n  Overall (last 28 days):")
                print(f"    Clicks:      {row.get('clicks', 0)}")
                print(f"    Impressions: {row.get('impressions', 0)}")
                print(f"    CTR:         {row.get('ctr', 0):.2%}")
                print(f"    Position:    {row.get('position', 0):.1f}")
                site_data["overall"] = row
            else:
                print("\n  No data for this period.")
        except Exception as e:
            print(f"  Error fetching overall: {e}")

        # Top queries
        body = {"startDate": "2026-01-26", "endDate": "2026-02-22", "dimensions": ["query"], "rowLimit": 25}
        try:
            data = gsc_request(access_token, f"sites/{encoded_site}/searchAnalytics/query", method="POST", body=body)
            if data.get("rows"):
                print(f"\n  Top Queries:")
                print(f"  {'Query':<40} {'Clicks':>8} {'Impr':>8} {'CTR':>8} {'Pos':>6}")
                print(f"  {'-'*40} {'-'*8} {'-'*8} {'-'*8} {'-'*6}")
                for row in data["rows"]:
                    q = row["keys"][0][:40]
                    print(f"  {q:<40} {row['clicks']:>8} {row['impressions']:>8} {row['ctr']:>7.1%} {row['position']:>6.1f}")
                site_data["queries"] = data["rows"]
        except Exception as e:
            print(f"  Error fetching queries: {e}")

        # Top pages
        body = {"startDate": "2026-01-26", "endDate": "2026-02-22", "dimensions": ["page"], "rowLimit": 25}
        try:
            data = gsc_request(access_token, f"sites/{encoded_site}/searchAnalytics/query", method="POST", body=body)
            if data.get("rows"):
                print(f"\n  Top Pages:")
                print(f"  {'Page':<60} {'Clicks':>8} {'Impr':>8} {'CTR':>8} {'Pos':>6}")
                print(f"  {'-'*60} {'-'*8} {'-'*8} {'-'*8} {'-'*6}")
                for row in data["rows"]:
                    p = row["keys"][0][-60:]
                    print(f"  {p:<60} {row['clicks']:>8} {row['impressions']:>8} {row['ctr']:>7.1%} {row['position']:>6.1f}")
                site_data["pages"] = data["rows"]
        except Exception as e:
            print(f"  Error fetching pages: {e}")

        # Top countries
        body = {"startDate": "2026-01-26", "endDate": "2026-02-22", "dimensions": ["country"], "rowLimit": 15}
        try:
            data = gsc_request(access_token, f"sites/{encoded_site}/searchAnalytics/query", method="POST", body=body)
            if data.get("rows"):
                print(f"\n  Top Countries:")
                print(f"  {'Country':<20} {'Clicks':>8} {'Impr':>8} {'CTR':>8} {'Pos':>6}")
                print(f"  {'-'*20} {'-'*8} {'-'*8} {'-'*8} {'-'*6}")
                for row in data["rows"]:
                    print(f"  {row['keys'][0]:<20} {row['clicks']:>8} {row['impressions']:>8} {row['ctr']:>7.1%} {row['position']:>6.1f}")
                site_data["countries"] = data["rows"]
        except Exception as e:
            print(f"  Error fetching countries: {e}")

        # Device breakdown
        body = {"startDate": "2026-01-26", "endDate": "2026-02-22", "dimensions": ["device"], "rowLimit": 5}
        try:
            data = gsc_request(access_token, f"sites/{encoded_site}/searchAnalytics/query", method="POST", body=body)
            if data.get("rows"):
                print(f"\n  Device Breakdown:")
                print(f"  {'Device':<20} {'Clicks':>8} {'Impr':>8} {'CTR':>8} {'Pos':>6}")
                print(f"  {'-'*20} {'-'*8} {'-'*8} {'-'*8} {'-'*6}")
                for row in data["rows"]:
                    print(f"  {row['keys'][0]:<20} {row['clicks']:>8} {row['impressions']:>8} {row['ctr']:>7.1%} {row['position']:>6.1f}")
                site_data["devices"] = data["rows"]
        except Exception as e:
            print(f"  Error fetching devices: {e}")

        # Daily trend
        body = {"startDate": "2026-01-26", "endDate": "2026-02-22", "dimensions": ["date"], "rowLimit": 28}
        try:
            data = gsc_request(access_token, f"sites/{encoded_site}/searchAnalytics/query", method="POST", body=body)
            if data.get("rows"):
                site_data["daily"] = data["rows"]
        except:
            pass

        all_site_data.append(site_data)

    # Save raw data
    with open("gsc_data.json", "w") as f:
        json.dump(all_site_data, f, indent=2)
    print("\n\nRaw data saved to gsc_data.json")


if __name__ == "__main__":
    main()
