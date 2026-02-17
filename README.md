# Tax Source of Truth

A curated, authoritative registry of public tax and accounting law sources.

Maintains a single source of truth for tax research and education workflows —
tracking primary sources by jurisdiction, authority type, and official status
with traceable citations back to the original publisher.

**Live demo:** https://nexusbluedev.github.io/tax-source-of-truth/

---

## What It Does

- Stores authoritative public URLs for tax law across federal, state, and city jurisdictions
- Enforces citation requirements — no facts without a primary source
- Provides a read-only search and retrieval layer with no inference or fuzzy logic
- Exposes an AI education layer (dormant) that requires citations in every response

## Current Coverage

| Jurisdiction | Sources |
|---|---|
| Federal | IRS Internal Revenue Bulletin, CFR Title 26 |
| Ohio (State) | Ohio Revised Code, Ohio Administrative Code, Ohio Dept of Taxation, RITA |
| Ohio (Cities) | Columbus, Dayton, Cincinnati income tax divisions |
| Florida (State) | Florida Statutes, Florida Administrative Code, Florida Dept of Revenue |

## Architecture

```
Supabase (PostgreSQL)
  └── source_registry table (RLS enabled, read-only via anon key)
        └── src/search.py       — deterministic query helpers, no inference
              └── src/ai_educator.py  — citation-enforced AI education layer (dormant)

index.html                      — static GitHub Pages demo UI (Supabase JS client)
```

## Stack

- **Database:** Supabase (PostgreSQL) with RLS enabled
- **Backend:** Python 3.12, Supabase Python client, python-dotenv
- **AI layer:** OpenAI (dormant — requires explicit OPENAI_API_KEY, manual trigger only)
- **Demo UI:** Static HTML + Supabase JS client, hosted on GitHub Pages
- **Code quality:** Black, Ruff, pre-commit hooks, GitHub Actions CI

## Local Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Copy `.env.example` to `.env` and fill in your Supabase credentials.

```powershell
# Verify database connection
python -m scripts.test_read_only

# Run search helpers
python -m scripts.test_search_helpers

# Run AI educator (no model calls)
python -m scripts.test_ai_educator
```

## Design Constraints

- **Read-only from Python** — no database writes from code; mutations require manual Supabase console access
- **No inference** — search layer returns exact matches only; no fuzzy logic or AI in the data retrieval path
- **Citations required** — AI education layer is explicitly constrained to return only source-backed answers
- **Anon key is public** — the Supabase anon key is intentionally read-only and safe to expose in the demo UI
- **AI is dormant** — OpenAI integration exists but requires explicit environment setup; no automated calls

## Repository

https://github.com/NexusBlueDev/tax-source-of-truth
