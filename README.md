# ory-python-demo

Minimal Python demo that calls the Ory Permission API to check access for a subject on an object in a namespace.

## What it does
- Configures `ory-client` with `ORY_BASE_URL` and a personal access token `ORY_TOKEN`
- Calls `check_permission` with `namespace`, `object`, `relation`, `subject_id`
- Prints the decision result

## Requirements
- Python 3.10+
- See shared prerequisites in `docs/PREREQS.md`

## Quickstart
git clone <your-repo-url> ory-python-demo
cd ory-python-demo
python3 -m venv .venv
. .venv/bin/activate
pip install ory-client

## Environment
export ORY_BASE_URL=https://playground.projects.oryapis.com
export ORY_TOKEN=<personal_access_token>

## Run
python check_permission.py --namespace docs --object page:123 --relation viewer --subject user:alice --max-depth 1

Expected output is a JSON-like structure including the decision field.

## VS Code
Use a launch config that selects `.venv` and sets `ORY_BASE_URL` and `ORY_TOKEN`.

## GitHub
- Setup Python and cache pip
- Create venv and install `ory-client`
- Run `python check_permission.py` with sample args
- Store `ORY_TOKEN` in Actions secrets

## Project structure
- `check_permission.py`
- `docs/PREREQS.md`
- `docs/ory-python-demo-architecture.svg`

## Diagram
## Diagram
![Ory Python Demo Architecture](docs/ory-python-demo-architecture.svg)

## License
MIT
