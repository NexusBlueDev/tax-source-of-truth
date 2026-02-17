from src.search import (
    list_all_sources,
    get_sources_by_jurisdiction,
    get_city_tax_authority,
    list_primary_sources,
)


print("=== ALL SOURCES ===")
for row in list_all_sources():
    print(
        row["jurisdiction_level"],
        "|",
        row["jurisdiction_name"],
        "|",
        row["source_name"],
    )

print("\n=== OHIO CITIES ===")
for row in get_sources_by_jurisdiction("city"):
    print(row["jurisdiction_name"], "|", row["source_name"])

print("\n=== CINCINNATI AUTHORITY ===")
for row in get_city_tax_authority("Cincinnati"):
    print(row["jurisdiction_name"], "|", row["source_name"])

print("\n=== PRIMARY SOURCES (OHIO) ===")
for row in list_primary_sources("Ohio"):
    print(row["jurisdiction_level"], "|", row["source_name"])
