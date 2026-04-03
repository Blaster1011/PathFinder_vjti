from django.shortcuts import render
from django.http import JsonResponse
from .engine.career_logic_engine import CareerLogicEngine
from .engine.ranking_engine import calculate_percentile
import json


def index(request):
    """Landing page with the student profile input form."""
    return render(request, "career/index.html")


def analyze(request):
    """
    POST endpoint: receives the student profile form, runs the full
    deterministic engine pipeline, and renders the dashboard.
    """
    if request.method != "POST":
        return render(request, "career/index.html")

    # ── Parse form data ───────────────────────────────────────────────────────
    name       = request.POST.get("name", "Student").strip() or "Student"
    year       = int(request.POST.get("year", 2))
    interest   = request.POST.get("interest", "AppDev")
    leetcode   = int(request.POST.get("leetcode", 0))
    cf_rating  = int(request.POST.get("cf_rating", 0))
    github     = int(request.POST.get("github_repos", 0))
    flutter_p  = int(request.POST.get("flutter_projects", 0))

    # Projects: comma-separated text input
    raw_projects = request.POST.get("projects", "")
    projects = [p.strip() for p in raw_projects.split(",") if p.strip()]

    profile = {
        "name":             name,
        "year":             year,
        "interest":         interest,
        "leetcode":         leetcode,
        "cf_rating":        cf_rating,
        "github_repos":     github,
        "projects":         projects,
        "flutter_projects": flutter_p,
    }

    # ── Run the engine ────────────────────────────────────────────────────────
    engine    = CareerLogicEngine(profile)
    readiness = engine.calculate_readiness()
    diagnosis = engine.diagnose_state()

    ranking   = calculate_percentile(
        user_score    = readiness["score"],
        user_year     = year,
        user_interest = interest,
    )

    roadmap   = engine.generate_roadmap(
        state        = diagnosis["state"],
        peer_top_pct = ranking["top_percent"],
    )

    # ── Build context for template ────────────────────────────────────────────
    context = {
        "profile":    profile,
        "readiness":  readiness,
        "diagnosis":  diagnosis,
        "ranking":    ranking,
        "roadmap":    roadmap,
        # For JS gauge — score as integer
        "score_int":  int(readiness["score"]),
        # Pretty interest label
        "interest_labels": {
            "AppDev": "App Development",
            "WebDev": "Web Development",
            "CP":     "Competitive Programming",
            "AI":     "AI / Machine Learning",
        },
        # Weights used (for display in trace panel)
        "weights": readiness["weights_used"],
    }
    return render(request, "career/dashboard.html", context)
