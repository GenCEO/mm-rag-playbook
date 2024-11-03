from mm_rag_playbook import build_chunks, score_chunks
from mm_rag_playbook.answering import draft_answer

PAGES = [
    "Vision-language pretraining aligns image and text spaces.",
    "Contrastive objectives improve retrieval for image-grounded QA.",
]


def main() -> None:
    q = "How does contrastive learning help retrieval?"
    chunks = build_chunks(PAGES)
    hits = score_chunks(q, chunks, top_k=4)
    print(draft_answer(q, hits))


if __name__ == "__main__":
    main()
