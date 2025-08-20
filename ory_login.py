# ory_login.py
import os, requests

BASE = os.getenv("BASE_URL", "https://dreamy-grothendieck-hgdo1j9d82.projects.oryapis.com")
IDENT = os.getenv("IDENT", "jonnadelberg")  # username in your cloud project
PASS = os.getenv("PASS", "X8v3qLr7fA2_9sNkT4")

def login(identifier: str, password: str):
    f = requests.get(f"{BASE}/self-service/login/api", timeout=10).json()["id"]
    r = requests.post(
        f"{BASE}/self-service/login?flow={f}",
        json={"method": "password", "identifier": identifier, "password": password},
        timeout=10,
    )
    r.raise_for_status()
    data = r.json()
    return data["session_token"], data["session"]["identity"]["id"]

def whoami(token: str):
    r = requests.get(f"{BASE}/sessions/whoami", headers={"X-Session-Token": token}, timeout=10)
    r.raise_for_status()
    return r.json()["identity"]["id"]

if __name__ == "__main__":
    tok, ident_id = login(IDENT, PASS)
    print("token:", tok[:24] + "…")
    me = whoami(tok)
    print("identity_id:", me)
