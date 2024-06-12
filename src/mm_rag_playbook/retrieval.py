from .pipeline import Chunk, RetrievalResult


def _token_overlap_score(query: str, content: str) -> float:
    q = {tok.lower() for tok in query.split() if tok.strip()}
    c = {tok.lower() for tok in content.split() if tok.strip()}
    if not q or not c:
        return 0.0
    return len(q & c) / len(q)


def score_chunks(query: str, chunks: list[Chunk], top_k: int = 4) -> list[RetrievalResult]:
    """Simple lexical scorer that works for both text and image summaries."""
    scored = [RetrievalResult(chunk=ch, score=_token_overlap_score(query, ch.content)) for ch in chunks]
    scored.sort(key=lambda item: item.score, reverse=True)
    return scored[:top_k]
