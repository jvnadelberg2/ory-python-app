#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
source .venv/bin/activate
export BASE_URL="https://dreamy-grothendieck-hgdo1j9d82.projects.oryapis.com"
export IDENT="jonnadelberg"
export PASS="X8v3qLr7fA2_9sNkT4"
python3 ory_login.py

