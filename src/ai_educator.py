"""
AI Education Layer (Read-Only)

Responsibilities:
- Accept a user question
- Retrieve authoritative sources via search helpers
- Produce an explanation grounded in retrieved sources
- Always return citations
- Never write data
"""

from typing import List, Dict
from src.search import (
    get_sources_by_jurisdiction,
    get_city_tax_authority,
    list_primary_sources,
)


class EducationResponse:
    def __init__(self, answer: str, sources: List[Dict]):
        self.answer = answer
        self.sources = sources


def explain_city_income_tax(city_name: str) -> EducationResponse:
    """
    Explain which authoritative sources govern income tax
    for a given city, without interpretation of law.
    """
    sources = get_city_tax_authority(city_name)

    if not sources:
        return EducationResponse(
            answer=f"No authoritative city income tax sources found for {city_name}.",
            sources=[],
        )

    answer_lines = [
        f"The following authoritative sources govern income tax for {city_name}:"
    ]

    for src in sources:
        answer_lines.append(f"- {src['source_name']} ({src['source_url']})")

    return EducationResponse(answer="\n".join(answer_lines), sources=sources)


def explain_state_tax_framework(state_name: str) -> EducationResponse:
    """
    Explain the authoritative tax framework for a state.
    """
    sources = list_primary_sources(state_name)

    if not sources:
        return EducationResponse(
            answer=f"No primary tax sources found for {state_name}.", sources=[]
        )

    answer_lines = [f"The authoritative tax framework for {state_name} includes:"]

    for src in sources:
        answer_lines.append(f"- {src['source_name']} ({src['authority_type']})")

    return EducationResponse(answer="\n".join(answer_lines), sources=sources)


import os
from openai import OpenAI


def explain_with_ai(question: str, sources: List[Dict]) -> EducationResponse:
    """
    Use an AI model to explain a question using ONLY the provided sources.
    The model is explicitly instructed not to invent facts or citations.
    """

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    if not sources:
        return EducationResponse(
            answer="No authoritative sources were available to answer this question.",
            sources=[],
        )

    client = OpenAI(api_key=api_key)

    source_context = "\n".join(
        f"- {s['source_name']}: {s.get('source_url', '')}" for s in sources
    )

    system_prompt = (
        "You are a tax education assistant.\n"
        "You must only use the provided authoritative sources.\n"
        "Do not invent rules, interpretations, or citations.\n"
        "If the sources do not answer the question, say so explicitly.\n"
    )

    user_prompt = (
        f"Question:\n{question}\n\n"
        f"Authoritative Sources:\n{source_context}\n\n"
        "Provide a clear explanation and cite the sources explicitly."
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.1,
    )

    answer_text = response.choices[0].message.content.strip()

    return EducationResponse(answer=answer_text, sources=sources)
