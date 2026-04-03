"""
RankingEngine — deterministic percentile calculation against mock peer dataset.
"""

from .career_logic_engine import CareerLogicEngine
from .peer_dataset        import MOCK_STUDENTS


def _score_peer(peer: dict) -> float:
    """Compute composite score for a single peer dict."""
    engine = CareerLogicEngine(peer)
    return engine.calculate_readiness()["score"]


def calculate_percentile(user_score: float, user_year: int, user_interest: str) -> dict:
    """
    Returns:
      - percentile      : what % of ALL peers the user outscores
      - top_percent     : 100 - percentile  (e.g. "Top 12%")
      - same_year_rank  : rank within same-year same-interest peers
      - peer_scores     : sorted list of (name, score) for the leaderboard
      - peers_total     : total peer count used
      - peers_beaten    : how many peers the user outscores
    """
    peer_scores = []
    for peer in MOCK_STUDENTS:
        s = _score_peer(peer)
        peer_scores.append({"name": peer["name"], "score": round(s, 1),
                             "year": peer["year"], "interest": peer["interest"]})

    beaten  = sum(1 for p in peer_scores if p["score"] < user_score)
    total   = len(peer_scores)
    pct     = round(beaten / total * 100, 1)
    top_pct = round(100 - pct, 1)

    # Same-year, same-interest cohort
    cohort = [p for p in peer_scores
              if p["year"] == user_year and p["interest"] == user_interest]
    cohort_beaten = sum(1 for p in cohort if p["score"] < user_score)
    cohort_total  = len(cohort) + 1   # +1 for the user
    cohort_rank   = cohort_total - cohort_beaten   # 1 = best

    # Sorted leaderboard (top 10 for display)
    leaderboard = sorted(peer_scores, key=lambda x: x["score"], reverse=True)[:10]

    return {
        "percentile":       pct,
        "top_percent":      top_pct,
        "cohort_rank":      cohort_rank,
        "cohort_total":     cohort_total,
        "leaderboard":      leaderboard,
        "peers_total":      total,
        "peers_beaten":     beaten,
    }
