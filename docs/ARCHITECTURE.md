# Architecture: ory-python-demo

![Ory Python Demo Architecture](./ory-python-demo-architecture.svg)

# Architecture: ory-python-demo

![Ory Python Demo Architecture](./ory-python-demo-architecture.svg)

_Figure: The Ory Python Demo architecture diagram shows a complete end-to-end login sequence.  
On the left, the local Python client (`ory_login.py`) runs in a shell environment configured with BASE_URL, IDENT, and PASS. Arrows trace the sequence of HTTPS requests: starting a login flow, submitting credentials, and retrieving a session token. On the right, the Ory Cloud project responds with JSON bodies that include the `flow id`, the `session_token`, and the `identity.id`.  

The loop concludes with the client verifying its own session via `/sessions/whoami`.  
This visual emphasizes that the client itself does not hold long-term state beyond the token and identity UUID, and that all validation and persistence remain inside Ory’s managed services._

---

## Purpose
Prove that a username/password login flow works against an Ory Cloud project and that the resulting session token can be validated.

- Start a login flow
- Submit credentials
- Receive a session token
- Call `whoami` to confirm the identity
- Print a truncated token and the identity ID

## Components
- **Client**: `ory_login.py` (Python 3.10+, uses `requests`)
- **Ory Project**: `https://<project-slug>.projects.oryapis.com`
- **Network**: HTTPS from client → Ory

## Environment parameters
These can override the in-file demo defaults.

- `BASE_URL` — Ory project base URL (e.g., `https://<slug>.projects.oryapis.com`)
- `IDENT` — identifier (email/username) for the test identity
- `PASS` — password for that identity

## Ory endpoints used
1. `GET /self-service/login/api` — start a login flow (returns `id`)
2. `POST /self-service/login?flow=<id>` — submit `{ "method": "password", "identifier": IDENT, "password": PASS }` (returns `session_token` and `session.identity.id`)
3. `GET /sessions/whoami` — header `X-Session-Token: <session_token>` (returns `identity.id`)

## Execution steps
1. Resolve configuration  
   Read `BASE_URL`, `IDENT`, `PASS` from the environment; if unset, use in-file demo defaults.
2. Start flow  
   `GET {BASE_URL}/self-service/login/api` → parse JSON → `flow_id = id`.
3. Submit credentials  
   `POST {BASE_URL}/self-service/login?flow={flow_id}` with JSON body:  
   { "method": "password", "identifier": IDENT, "password": PASS }  
   On success, capture `session_token` and `session.identity.id`.
4. Verify session  
   `GET {BASE_URL}/sessions/whoami` with `X-Session-Token: <session_token>` → read `identity.id`.
5. Output  
   Print:  
   - token: first ~24 chars + ellipsis (truncated)  
   - identity_id: the UUID

## Inputs / outputs
- Inputs: env vars `BASE_URL`, `IDENT`, `PASS` (optional if using defaults)
- Outputs: two stdout lines:
  - token: ory_st_…
  - identity_id: <uuid>

## Error handling
- Non-2xx responses raise for status and exit non-zero.
- Common issues:
  - 401 — wrong IDENT/PASS
  - 404 — incorrect BASE_URL/project slug
  - Network errors — DNS, proxy, firewall

## Security note
Defaults in `ory_login.py` exist so the demo runs immediately. They are demo-only. For anything beyond this demo, set BASE_URL, IDENT, and PASS via environment variables (or delete the defaults) and never commit real credentials.

## Minimal run
One-time setup:
python3 -m pip install -r requirements.txt

Run:
python3 ory_login.py

Override with your own values if needed:
export BASE_URL="https://<slug>.projects.oryapis.com"
export IDENT="your-identifier"
export PASS="your-password"
python3 ory_login.py

## Simple sequence (text)
Client → GET /self-service/login/api → Ory  
Client → POST /self-service/login?flow=<id> (credentials) → Ory  
Client → GET /sessions/whoami

---

## Notes for extension
This demo is intentionally minimal. To extend:
- Add error-handling for rate limiting or network retries.
- Demonstrate logout (`DELETE /sessions`).
- Use the SDKs (`ory-client` for Python) instead of raw `requests`.
- Integrate into a web framework (FastAPI, Flask) for real applications.

## Summary
This architecture validates the essential login/session lifecycle against Ory Cloud:
- Start login flow
- Submit credentials
- Get session token and identity
- Confirm session via `whoami`

The combination of diagram and stepwise execution provides a reproducible reference for anyone testing Ory authentication from Python.

---

## Purpose
Prove that a username/password login flow works against an Ory Cloud project and that the resulting session token can be validated.

- Start a login flow
- Submit credentials
- Receive a session token
- Call `whoami` to confirm the identity
- Print a truncated token and the identity ID

## Components
- **Client**: `ory_login.py` (Python 3.10+, uses `requests`)
- **Ory Project**: `https://<project-slug>.projects.oryapis.com`
- **Network**: HTTPS from client → Ory

## Environment parameters
These can override the in-file demo defaults.

- `BASE_URL` — Ory project base URL (e.g., `https://<slug>.projects.oryapis.com`)
- `IDENT` — identifier (email/username) for the test identity
- `PASS` — password for that identity

## Ory endpoints used
1. `GET /self-service/login/api` — start a login flow (returns `id`)
2. `POST /self-service/login?flow=<id>` — submit `{ "method": "password", "identifier": IDENT, "password": PASS }` (returns `session_token` and `session.identity.id`)
3. `GET /sessions/whoami` — header `X-Session-Token: <session_token>` (returns `identity.id`)

## Execution steps
1. Resolve configuration  
   Read `BASE_URL`, `IDENT`, `PASS` from the environment; if unset, use in-file demo defaults.
2. Start flow  
   `GET {BASE_URL}/self-service/login/api` → parse JSON → `flow_id = id`.
3. Submit credentials  
   `POST {BASE_URL}/self-service/login?flow={flow_id}` with JSON body:  
   { "method": "password", "identifier": IDENT, "password": PASS }  
   On success, capture `session_token` and `session.identity.id`.
4. Verify session  
   `GET {BASE_URL}/sessions/whoami` with `X-Session-Token: <session_token>` → read `identity.id`.
5. Output  
   Print:  
   - token: first ~24 chars + ellipsis (truncated)  
   - identity_id: the UUID

## Inputs / outputs
- Inputs: env vars `BASE_URL`, `IDENT`, `PASS` (optional if using defaults)
- Outputs: two stdout lines:
  - token: ory_st_…
  - identity_id: <uuid>

## Error handling
- Non-2xx responses raise for status and exit non-zero.
- Common issues:
  - 401 — wrong IDENT/PASS
  - 404 — incorrect BASE_URL/project slug
  - Network errors — DNS, proxy, firewall

## Security note
Defaults in `ory_login.py` exist so the demo runs immediately. They are demo-only. For anything beyond this demo, set BASE_URL, IDENT, and PASS via environment variables (or delete the defaults) and never commit real credentials.

## Minimal run
One-time setup:
python3 -m pip install -r requirements.txt

Run:
python3 ory_login.py

Override with your own values if needed:
export BASE_URL="https://<slug>.projects.oryapis.com"
export IDENT="your-identifier"
export PASS="your-password"
python3 ory_login.py

## Simple sequence (text)
Client → GET /self-service/login/api → Ory  
Client → POST /self-service/login?flow=<id> (credentials) → Ory  
Client → GET /sessions/whoami

---

## Notes for extension
This demo is intentionally minimal. To extend:
- Add error-handling for rate limiting or network retries.
- Demonstrate logout (`DELETE /sessions`).
- Use the SDKs (`ory-client` for Python) instead of raw `requests`.
- Integrate into a web framework (FastAPI, Flask) for real applications.

## Summary
This architecture validates the essential login/session lifecycle against Ory Cloud:
- Start login flow
- Submit credentials
- Get session token and identity
- Confirm session via `whoami`

The combination of diagram and stepwise execution provides a reproducible reference for anyone testing Ory authentication from Python.
