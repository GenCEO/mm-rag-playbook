from mm_rag_playbook import build_chunks, score_chunks
from mm_rag_playbook.config import RetrievalConfig, filter_results

PAGES = [
    """
    Transformer models use multi-head attention.
    Figure 1 compares sparse and dense attention maps.
    """,
    """
    Retrieval-augmented generation improves factual grounding.
    We index captions and paragraph chunks jointly.
    """,
]


def main() -> None:
    chunks = build_chunks(PAGES)
    query = "multi-head attention figure"
    results = score_chunks(query=query, chunks=chunks, top_k=6)
    results = filter_results(results, RetrievalConfig(top_k=3, min_score=0.1))
    for r in results:
        print(f"{r.chunk.chunk_id:10s} | {r.chunk.modality:5s} | score={r.score:.2f}")
        print(f"  {r.chunk.content[:90]}")


if __name__ == "__main__":
    main()
