# Python Project Template

Reusable Python project template for NexusBlue development on Windows.

This template assumes:
- Python is already installed
- Git is configured
- GitHub SSH authentication is set up
- Projects live under OneDrive for backup

Authoritative setup documentation lives in SETUP.md.
---

## Template Status

This repository is a stable Python project template for NexusBlue.

Tooling (formatting, linting, CI, VS Code integration) is considered complete.
Only project-specific code should be added when using this template.

---

## Quick Start (After Using This Template)

After creating a new repository from this template and cloning it locally:

```powershell
cd <project-directory>
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

---

## Pre-commit Hooks

This project uses pre-commit to enforce formatting and linting.

Hooks run automatically before every commit.

To run manually:

```powershell
pre-commit run --all-files

If needed, hooks can be bypassed with:

git commit --no-verify


Save and close.

---

## STEP 6: Commit and push

Run:

```powershell
git status
git add .pre-commit-config.yaml requirements-dev.txt README.md
git commit -m "Add pre-commit hooks for formatting and linting"
git push

---
