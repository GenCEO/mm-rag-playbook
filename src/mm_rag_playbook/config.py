from dataclasses import dataclass


@dataclass
class RetrievalConfig:
    top_k: int = 4
    min_score: float = 0.05


def filter_results(results, cfg: RetrievalConfig):
    return [r for r in results[: cfg.top_k] if r.score >= cfg.min_score]
