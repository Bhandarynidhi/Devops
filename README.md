# DevSecOps Challenge - Flask API

Simple Flask API used for a CI/CD + security checks demo.

[![CI](https://github.com/USERNAME/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/USERNAME/REPO/actions)
[![CodeQL](https://github.com/USERNAME/REPO/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/USERNAME/REPO/actions)

## Run locally
1. python -m venv .venv
2. Activate and install:
   - Windows: `.venv\Scripts\Activate.ps1`
   - macOS/Linux: `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python app.py`
5. Visit http://127.0.0.1:5000/

## CI / Security
This repo includes:
- flake8 (lint)
- pytest (unit tests)
- bandit (static security scan)
- CodeQL (GitHub code scanning)
- Gitleaks (secret scanning)

Replace `USERNAME` and `REPO` above with your GitHub username and repository name to show the badges.
