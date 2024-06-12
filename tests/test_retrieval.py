from mm_rag_playbook import build_chunks, score_chunks


def test_retrieval_prefers_relevant_chunks() -> None:
    chunks = build_chunks(["multi-head attention details", "retrieval database notes"])
    top = score_chunks("attention", chunks, top_k=1)[0]
    assert "attention" in top.chunk.content.lower()
