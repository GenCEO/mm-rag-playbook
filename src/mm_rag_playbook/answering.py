from .pipeline import RetrievalResult


def build_context(results: list[RetrievalResult]) -> str:
    lines: list[str] = []
    for rank, item in enumerate(results, start=1):
        lines.append(
            f"[{rank}] ({item.chunk.modality}) p{item.chunk.source_page}: {item.chunk.content[:160]}"
        )
    return "\n".join(lines)


def draft_answer(question: str, results: list[RetrievalResult]) -> str:
    context = build_context(results)
    return (
        f"Question: {question}\n"
        f"Evidence:\n{context}\n"
        "Synthesis: The most relevant evidence is ranked first; combine text and figure summaries."
    )
