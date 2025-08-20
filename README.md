# ory-python-demo

Python demo that logs in to Ory Cloud and prints a session token and identity ID.

## Requirements
- Python 3.10+
- requests library
- Ory Cloud project (see BASE_URL, IDENT, PASS in ory_login.py)

## One-time setup
python3 -m pip install --user -r requirements.txt

## Run
python3 ory_login.py

Expected output:
token: ory_st_…
identity_id: <uuid>

## Project structure
- ory_login.py — demo script
- requirements.txt — dependencies (requests only)
- docs/ory-python-demo-architecture.svg — architecture diagram

## Diagram
![Ory Python Demo Architecture](docs/ory-python-demo-architecture.svg)

## License
MIT
