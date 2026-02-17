"""
WARNING:
This script makes a REAL OpenAI API call.
Run only after setting OPENAI_API_KEY in your .env file.
"""

from src.ai_educator import explain_with_ai
from src.search import get_city_tax_authority


city = "Cincinnati"
question = "What authority governs municipal income tax for this city?"

sources = get_city_tax_authority(city)

response = explain_with_ai(
    question=question,
    sources=sources,
)

print("=== AI ANSWER ===")
print(response.answer)

print("\n=== CITED SOURCES ===")
for src in response.sources:
    print("-", src["source_name"], "|", src.get("source_url", ""))
