# mm-rag-playbook

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![Stage](https://img.shields.io/badge/Stage-Research%20Prototype-0A7E07) ![License](https://img.shields.io/badge/License-MIT-1f6feb)


A compact research playground for **multimodal RAG** on PDF-like documents.

## Why
- Build a minimal but clear dataflow: parse -> chunk -> retrieve -> answer
- Keep text and image channels side-by-side for debugging
- Offer reproducible examples that can be extended to full VLM stacks

## Ideas borrowed and refined
- From lightweight PyMuPDF4LLM demos: keep the end-to-end path small and inspectable
- From modern multimodal systems: represent image evidence as first-class retrieval units

## Quickstart
```bash
pip install -e .
python examples/run_demo.py
```

## Project layout
- `src/mm_rag_playbook/pipeline.py`: chunk construction
- `src/mm_rag_playbook/retrieval.py`: retrieval scoring
- `examples/run_demo.py`: runnable local demo
- `tests/test_retrieval.py`: minimal sanity checks
