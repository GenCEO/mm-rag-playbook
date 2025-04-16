# Research Notes

## Retrieval recipe
1. Convert pages into text chunks and image summaries.
2. Score both modalities with the same API first.
3. Keep modality tags in output for later reranking.

## Next ideas
- Replace lexical scoring with CLIP or SigLIP embeddings.
- Add metadata filters for section and figure IDs.
