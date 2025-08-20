# ory-python-demo

Minimal Python demo that calls the Ory Permission API to check access for a subject on an object in a namespace.

## What it does
- Configures `ory-client` with `ORY_BASE_URL` and a personal access token `ORY_TOKEN`
- Calls `check_permission` with `namespace`, `object`, `relation`, `subject_id`
- Prints the decision result

## Requirements
- Python 3.10+
- An Ory Network project or the public playground
- A personal access token with permission API access
- Environment variables:
  - `ORY_BASE_URL` (default: `https://playground.projects.oryapis.com`)
  - `ORY_TOKEN` (required)

## Quickstart

```bash
git clone <your-repo-url> ory-python-demo
cd ory-python-demo
pip install --user ory-client
export ORY_BASE_URL=https://playground.projects.oryapis.com
export ORY_TOKEN=<personal_access_token>
python check_permission.py --namespace docs --object page:123 --relation viewer --subject user:alice --max-depth 1
