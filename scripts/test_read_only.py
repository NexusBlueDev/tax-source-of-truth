import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_ANON_KEY")

if not url or not key:
    raise RuntimeError("Missing SUPABASE_URL or SUPABASE_ANON_KEY")

supabase = create_client(url, key)

response = (
    supabase.table("source_registry")
    .select("jurisdiction_level, jurisdiction_name, source_name")
    .order("jurisdiction_level")
    .execute()
)

for row in response.data:
    print(
        f"{row['jurisdiction_level']} | "
        f"{row['jurisdiction_name']} | "
        f"{row['source_name']}"
    )
