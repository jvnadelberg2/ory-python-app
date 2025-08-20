# Security Policy

## Supported Versions
This demo is provided as-is for illustrative purposes. It is not a production system and does not receive security updates.

## Credentials and Secrets
- Do not commit personal access tokens, passwords, or other secrets into the repository.
- When running locally, provide required values (e.g., `BASE_URL`, `IDENT`, `PASS`) as environment variables.
- For GitHub Actions or CI, store values in **Repository Settings → Secrets and variables → Actions**.

## Reporting Issues
This repository is for demonstration. Security issues in Ory Cloud itself should be reported through Ory’s official support channels.

## Disclaimer
The code here is simplified to show how to call Ory APIs. It does not include full security practices such as token management, secret rotation, or error handling that would be required in a real application.
