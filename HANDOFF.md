# HANDOFF.md

## Project
Tax Source of Truth System

## Purpose
Build a Windows-based Python system that maintains a curated, authoritative,
time-aware registry of public accounting and tax law sources.

The system must:
- Use only public, authoritative URLs
- Track sources by jurisdiction, tax type, year, and effective date
- Support research, education, and accuracy-critical workflows
- Provide traceable citations back to primary sources

## Initial Jurisdiction Scope
- Federal (United States)
- Ohio
  - State-level tax law and guidance
  - Cities: Columbus, Dayton, Cincinnati
  - South Ohio corridor municipalities (RITA and self-administered)
- Florida
  - State-level tax law and guidance

## Infrastructure

### Database
- Provider: Supabase (Postgres)
- Project name: tax-source-of-truth
- Project URL: https://easdflriuxduqpmivfip.supabase.co

Notes:
- Supabase is the system of record for authoritative source data
- No secrets are stored in the repository
- Connection keys will be managed via environment variables later

## Development Constraints
- Windows-based Python workflow
- Built from python-project-template
- Source accuracy over convenience
- No assumptions without citations
- Incremental, auditable development
- One action per step

## Current State

- Supabase is the system of record for authoritative tax sources
- source_registry table implemented, seeded, and verified (12 rows)
- Schema defined in docs/schema.md
- Seed plan defined in docs/seed_plan.md
- Python 3.12 virtual environment configured
- Read-only Supabase access verified from Python
- Deterministic search and retrieval layer implemented (src/search.py)
- AI education layer implemented with citation enforcement (src/ai_educator.py)
- OpenAI integration present but dormant and manually triggered only
- No automation, no RLS, and no database writes from Python

## Database State

- Supabase table: source_registry
- Schema implemented and matches docs/schema.md
- Seeded and verified
- Total rows: 12
- Coverage:
  - Federal: IRS IRB, CFR Title 26
  - Ohio (State): ORC, OAC, Ohio Department of Taxation, Regional Income Tax Agency (RITA)
  - Ohio (City): Columbus Income Tax Division, Dayton Income Tax Division, Cincinnati Income Tax Division
  - Florida: Florida Statutes, Florida Administrative Code, Florida Department of Revenue
- All sources marked primary and active
- No RLS, policies, automation, or write access from Python

## Python Access

- Python 3.12 virtual environment configured
- Supabase Python client installed
- python-dotenv installed
- Read-only access verified using anon public key
- Test script: scripts/test_read_only.py
- Successful SELECT against source_registry
- No write, update, or delete operations enabled
- .env is git-ignored and contains Supabase credentials

## Search and Retrieval Layer

- Deterministic Python search helpers implemented
- Module: src/search.py
- Supports jurisdiction-based and city-level queries
- No AI or inference logic included
- Read-only Supabase access enforced
- Test script: scripts/test_search_helpers.py
- Verified via module execution (python -m scripts.test_search_helpers)
- Designed for future AI consumption with guaranteed source retrieval

## AI Education Layer (Read-Only)

- AI education layer skeleton implemented
- Module: src/ai_educator.py
- Education functions retrieve data exclusively via search helpers
- Answers always include authoritative source citations
- No AI model calls yet
- No database writes
- Test script: scripts/test_ai_educator.py
- Verified via module execution (python -m scripts.test_ai_educator)
- Designed for future controlled AI integration and human review

## AI Model Integration (Dormant)

- OpenAI client integrated for education layer
- Integration is read-only and citation-enforced
- No AI calls executed to date
- Execution requires explicit environment configuration (OPENAI_API_KEY)
- Live test harness exists: scripts/test_ai_live.py
- AI usage is intentional, auditable, and manually triggered
- No database writes or automated execution paths

## Next Logical Phases (Not Executed)

### High-confidence recommended sequence (demo-first)

1. Build UI for user test and demo (next)
   - Use Streamlit for an internal demo UI
   - Read-only first
   - Capabilities:
     - Search and explore jurisdictions and sources
     - Ask AI questions (education mode, citations required)
   - No writes in the initial UI milestone

2. Add Admin UI (controlled writes)
   - Add and edit jurisdictions, sources, and authorities
   - Manual save only
   - Explicit authoritative tagging (statute, regulation, agency guidance)
   - No automation

3. Add RITA management
   - City-to-RITA membership mapping
   - Admin-only changes
   - Integrate mapping into search and AI context

4. Demo hardening
   - Demo and user-test mode
   - Disclaimers and guardrails
   - Predictable demo flows
   - Separation of read vs manage modes

5. Publish to GitHub
   - After UI MVP exists
   - Add README describing:
     - Architecture
     - Safety constraints
     - AI usage policy (manual, citation-enforced)

6. Monitoring metadata (schema-level only)
   - Update cadence
   - Effective date
   - Last reviewed
   - Change detection method
   - Still no automation

7. Change detection (implementation)
   - Start with 1–2 sources (IRS IRB, Ohio Department of Taxation)
   - Diff and alert only
   - No auto-write without approval

8. Expand jurisdictions
   - Additional Ohio municipalities
   - Florida municipalities and counties as needed

## Immediate Next Goal

Build a read-only UI suitable for internal user testing and demos.

- Implement a Streamlit-based UI
- Support search and exploration of jurisdictions and sources
- Enable AI-assisted education with citations
- No write access in the initial UI phase

## Open Questions

- UI framework confirmation (Streamlit vs future React)
- Admin permission model for managing sources
- Review and approval workflow for AI-generated explanations
- Scope and cadence of future change detection

## Last Updated
2026-01-01
