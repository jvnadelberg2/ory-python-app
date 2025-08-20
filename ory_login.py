import os
import requests

BASE = os.environ.get("BASE_URL", "http://127.0.0.1:4433")

def login(identifier: str, password: str):
    # Start a new login flow
    r = requests.get(f"{BASE}/self-service/login/api", timeout=5)
    r.raise_for_status()
    fid = r.json()["id"]

    # Submit login credentials
    r2 = requests.post(
        f"{BASE}/self-service/login",
        params={"flow": fid},
        json={"method": "password", "identifier": identifier, "password": password},
        timeout=5,
    )
    r2.raise_for_status()
    d = r2.json()
    return d["session_token"], d["session"]["identity"]

def whoami(token: str):
    r = requests.get(
        f"{BASE}/sessions/whoami",
        headers={"X-Session-Token": token},
        timeout=5,
    )
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    tok, ident = login("jon+test@example.com", "X8!v3qLr7fA2_9sN$kT4")
    print("token:", tok[:24] + "…")
    me = whoami(tok)
    print("identity_id:", me["identity"]["id"])
