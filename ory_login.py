# ory_login.py
#
# Demo script for Ory Cloud.
# Logs in with username/password, obtains a session token,
# and verifies the identity via the Ory API.
#
# SECURITY NOTE:
# These defaults (IDENT, PASS) are demo-only and included so the
# script runs out of the box. Do not reuse them outside this demo.
# For real use, set BASE_URL, IDENT, and PASS as environment variables.

import os, requests

# BASE is the Ory project URL.
BASE = os.getenv("BASE_URL", "https://dreamy-grothendieck-hgdo1j9d82.projects.oryapis.com")

# Demo identifier and password, also overridable with environment variables
IDENT = os.getenv("IDENT", "jonnadelberg")
PASS = os.getenv("PASS", "X8v3qLr7fA2_9sNkT4")

def login(identifier: str, password: str):
    # Start a login flow (Ory: /self-service/login/api)
    f = requests.get(f"{BASE}/self-service/login/api", timeout=10).json()["id"]

    # Submit credentials to complete the flow (Ory: /self-service/login?flow=...)
    r = requests.post(
        f"{BASE}/self-service/login?flow={f}",
        json={"method": "password", "identifier": identifier, "password": password},
        timeout=10,
    )
    r.raise_for_status()
    data = r.json()
    return data["session_token"], data["session"]["identity"]["id"]

def whoami(token: str):
    # Validate the session token and fetch identity (Ory: /sessions/whoami)
    r = requests.get(f"{BASE}/sessions/whoami", headers={"X-Session-Token": token}, timeout=10)
    r.raise_for_status()
    return r.json()["identity"]["id"]

if __name__ == "__main__":
    tok, ident_id = login(IDENT, PASS)
    print("token:", tok[:24] + "…")   # print a truncated token for safety
    me = whoami(tok)
    print("identity_id:", me)
