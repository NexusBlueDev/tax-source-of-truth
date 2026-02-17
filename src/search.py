import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()


def _get_client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_ANON_KEY")

    if not url or not key:
        raise RuntimeError("Missing SUPABASE_URL or SUPABASE_ANON_KEY")

    return create_client(url, key)


def list_all_sources():
    """
    Return all sources in the registry.
    Intended for diagnostics and completeness checks.
    """
    supabase = _get_client()
    return (
        supabase.table("source_registry")
        .select("*")
        .order("jurisdiction_level")
        .execute()
        .data
    )


def get_sources_by_jurisdiction(
    jurisdiction_level: str, jurisdiction_name: str | None = None
):
    """
    Retrieve sources filtered by jurisdiction level,
    optionally narrowed to a specific jurisdiction name.
    """
    supabase = _get_client()
    query = (
        supabase.table("source_registry")
        .select("*")
        .eq("jurisdiction_level", jurisdiction_level)
    )

    if jurisdiction_name:
        query = query.eq("jurisdiction_name", jurisdiction_name)

    return query.execute().data


def get_city_tax_authority(city_name: str):
    """
    Retrieve the authoritative tax source for a given city.
    """
    supabase = _get_client()
    return (
        supabase.table("source_registry")
        .select("*")
        .eq("jurisdiction_level", "city")
        .ilike("jurisdiction_name", f"%{city_name}%")
        .execute()
        .data
    )


def list_primary_sources(state: str | None = None):
    """
    List all primary sources, optionally filtered by state.
    """
    supabase = _get_client()
    query = (
        supabase.table("source_registry").select("*").eq("official_status", "primary")
    )

    if state:
        query = query.eq("jurisdiction_name", state)

    return query.execute().data
