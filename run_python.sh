#!/usr/bin/env bash
set -euo pipefail

pip install -r requirements.txt
python3 ory_login.py
