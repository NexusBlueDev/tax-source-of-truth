from src.ai_educator import (
    explain_city_income_tax,
    explain_state_tax_framework,
)


print("=== CITY EDUCATION: CINCINNATI ===")
city_response = explain_city_income_tax("Cincinnati")
print(city_response.answer)
print("Sources:")
for src in city_response.sources:
    print("-", src["source_name"], "|", src["source_url"])

print("\n=== STATE EDUCATION: OHIO ===")
state_response = explain_state_tax_framework("Ohio")
print(state_response.answer)
print("Sources:")
for src in state_response.sources:
    print("-", src["source_name"], "|", src["authority_type"])
