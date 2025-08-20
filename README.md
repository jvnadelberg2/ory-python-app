# ory-python-demo

Python demo that logs in to Ory Cloud and prints a session token and identity ID.

## Requirements
- Python 3.10+
- `requests` library
- Ory Cloud project (see `BASE_URL`, `IDENT`, `PASS` in `ory_login.py`)

## Environment

\`\`\`bash
export BASE_URL=https://<your-project-slug>.projects.oryapis.com
export IDENT=<your-identity-username>
export PASS=<your-password>
\`\`\`

## Run

\`\`\`bash
python3 ory_login.py
\`\`\`

Expected output includes a session token (truncated for readability) and the identity ID.

## VS Code
Use a launch config that sets `BASE_URL`, `IDENT`, and `PASS`.

## GitHub
- Setup Python and cache pip
- Store secrets (`BASE_URL`, `IDENT`, `PASS`) in GitHub Actions → Settings → Secrets
- Run `python ory_login.py` with sample args in CI

## Project structure
- `ory_login.py` – demo script with login and whoami calls
- `requirements.txt` – Python dependencies
- `README.md` – usage guide
- `ARCHITECTURE.md` – explanation of flow and diagram
- `SECURITY.md` – security policy
- `LICENSE` – MIT license

## License
MIT License. See [LICENSE](LICENSE) for details.

## Security
For information about handling secrets and security considerations, see [SECURITY.md](SECURITY.md).
