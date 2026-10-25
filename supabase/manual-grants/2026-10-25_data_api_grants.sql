-- tax-source-of-truth: Supabase Data API grant formalization
-- Project ref: easdflriuxduqpmivfip
-- Applied live via Supabase Management API on 2026-10-25 (NOT a migration file --
-- this repo has no migrations directory / migration-as-code discipline at all,
-- see the companion finding filed in setup_blockers for that separate, larger gap).
--
-- Part of the platform-wide Supabase Data API Grant Audit program
-- (nexusblue-core: docs/roadmap/SUPABASE_DATA_API_GRANT_AUDIT.md). Supabase
-- removes the automatic Data API grant on public-schema tables for every
-- existing project on 2026-10-30. This file is the durable, git-tracked record
-- of what was applied directly to production, kept here (instead of only
-- existing as a Management API call with no local trace) per Rule #69 architect
-- review (CONDITIONAL PASS -- the one condition was exactly this: commit the
-- script for a recordkeeping trail since no migration file exists).
--
-- Live-queried state at time of derivation (2026-10-25):
--   public schema contains exactly ONE relation: source_registry (ordinary
--   table, relkind='r'). No views, materialized views, or partitioned tables
--   exist in this project.
--   rowsecurity = true on source_registry.
--   Exactly one policy: "Enable read access for all users",
--     roles={public} (covers anon AND authenticated), cmd=SELECT, qual=true,
--     with_check=null. No INSERT/UPDATE/DELETE policy exists for any role --
--     anon/authenticated cannot write today and this script does not change
--     that.
--
-- This matches the repo's own documented intent (HANDOFF.md: "RLS enabled on
-- source_registry; 'Enable read access for all users' policy active"; the
-- GitHub Pages demo UI "Uses Supabase JS client with anon key (read-only, safe
-- to expose)"). The table stores only a curated list of public, authoritative
-- tax-law source URLs (IRS, state/city tax agency links) -- not taxpayer
-- records or financial data, despite the repo's name.
--
-- Verified applied via information_schema.role_table_grants subset-containment
-- check immediately after running this: 0 failures (service_role has ALL,
-- authenticated has SELECT, anon has SELECT).

-- service_role: standard full access (bypasses RLS entirely; always granted ALL
-- across every repo in this program, matches core_rules #315).
GRANT ALL ON public.source_registry TO service_role;

-- authenticated: matches the real, unconditional SELECT policy (roles={public}
-- includes authenticated). No write policy exists for authenticated, so no
-- write grant is issued.
GRANT SELECT ON public.source_registry TO authenticated;

-- anon: matches the real, unconditional SELECT policy (roles={public} includes
-- anon). This is the exact access path the GitHub Pages demo UI already uses
-- today via the anon key. No write policy exists for anon, so no write grant
-- is issued.
GRANT SELECT ON public.source_registry TO anon;
