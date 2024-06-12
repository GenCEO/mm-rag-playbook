from dataclasses import dataclass
from typing import Iterable


@dataclass
class Chunk:
    chunk_id: str
    modality: str
    content: str
    source_page: int


@dataclass
class RetrievalResult:
    chunk: Chunk
    score: float


def build_chunks(pages: Iterable[str]) -> list[Chunk]:
    """Split pages into text chunks and create synthetic image placeholders."""
    chunks: list[Chunk] = []
    for i, page in enumerate(pages, start=1):
        lines = [ln.strip() for ln in page.splitlines() if ln.strip()]
        text_body = " ".join(lines)
        chunks.append(
            Chunk(
                chunk_id=f"p{i}-text",
                modality="text",
                content=text_body,
                source_page=i,
            )
        )
        chunks.append(
            Chunk(
                chunk_id=f"p{i}-image",
                modality="image",
                content=f"Figure summary from page {i}: {text_body[:80]}",
                source_page=i,
            )
        )
    return chunks
