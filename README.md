# ory-python-demo

Python demo that logs in to Ory Network and validates a session.

## Purpose

This project demonstrates two approaches:

1. Login via REST API using `requests`
   - Calls /self-service/login/api to start a flow.
   - Calls /self-service/login?flow=<id> to submit credentials.
   - Returns a session_token and identity.id.

2. Validate session via SDK using `ory-client`
   - Calls FrontendApi.to_session(x_session_token=...).
   - Wraps the REST endpoint /sessions/whoami.

## Requirements

- Python 3.10+
- Packages listed in requirements.txt:
  - requests
  - ory-client

## Setup

Clone this repo and create a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Environment

Set the following variables before running. Do not include < > in the values.

    export BASE_URL="https://<project-slug>.projects.oryapis.com"
    export IDENT="your-username"
    export PASS="your-password"

Example:

    export BASE_URL="https://myproj-abc123.projects.oryapis.com"
    export IDENT="jonnadelberg"
    export PASS="example-password"

## Run

    python ory_login.py

Expected output (values truncated for safety):

    token: ory_st_ABC123…
    identity_id: 8f268dd1-3ec3-43ed-83f3-cfd469fb8906

## Project structure

- ory_login.py — demo script (REST login + SDK whoami)
- requirements.txt — dependencies
- README.md — usage guide
- docs/ARCHITECTURE.md — architecture overview
- docs/SECURITY.md — security notes
- LICENSE — MIT license

## License

MIT License. See LICENSE for details.
