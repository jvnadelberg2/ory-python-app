# ory_login.py
# Login via raw HTTP (requests), then whoami via official Ory Python SDK.

import os
import requests
import ory_client
from ory_client import Configuration, ApiClient
from ory_client.api import frontend_api

# BASE is the Ory project URL.
BASE = os.getenv("BASE_URL", "https://dreamy-grothendieck-hgdo1j9d82.projects.oryapis.com")

# Demo identifier and password, also overridable with environment variables
IDENT = os.getenv("IDENT", "jonnadelberg")
PASS = os.getenv("PASS", "X8v3qLr7fA2_9sNkT4")


def login(username: str, password: str):
    # Start login flow
    r = requests.get(f"{BASE}/self-service/login/api", timeout=10)
    r.raise_for_status()
    flow = r.json()["id"]

    # Submit credentials
    r = requests.post(
        f"{BASE}/self-service/login?flow={flow}",
        json={"identifier": username, "password": password, "method": "password"},
        timeout=10,
    )
    r.raise_for_status()
    data = r.json()
    return data["session_token"], data["session"]["identity"]["id"]

def whoami_sdk(token: str) -> str:
    cfg = Configuration(host=BASE)
    with ApiClient(cfg) as api:
        fe = frontend_api.FrontendApi(api)
        session = fe.to_session(x_session_token=token)
        return session.identity.id

if __name__ == "__main__":
    if not (IDENT and PASS and BASE):
        raise SystemExit("Set BASE_URL, IDENT, PASS environment variables.")
    tok, ident_id = login(IDENT, PASS)
    print("token:", tok[:24] + "…")
    me = whoami_sdk(tok)
    print("identity_id:", me)
