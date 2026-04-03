"""
CareerLogicEngine — 100% Deterministic, Zero LLM.
All scoring, decision trees, and state machine logic lives here.
"""

# ── Normalization ceilings (used to map raw stats → 0–1 scale) ────────────────
NORM = {
    "leetcode":    700,   # considered "maxed out" for scoring purposes
    "cf_rating":  2400,   # grandmaster threshold
    "github":      20,
    "projects":     5,
}

# ── Interest-specific weight tables ───────────────────────────────────────────
WEIGHTS = {
    "AppDev": {
        "leetcode":        0.20,
        "cf_rating":       0.05,
        "github_repos":    0.10,
        "projects":        0.35,
        "flutter_bonus":   0.30,   # extra weight if Flutter projects present
    },
    "WebDev": {
        "leetcode":        0.20,
        "cf_rating":       0.05,
        "github_repos":    0.30,
        "projects":        0.40,
        "flutter_bonus":   0.05,
    },
    "CP": {
        "leetcode":        0.20,
        "cf_rating":       0.70,
        "github_repos":    0.05,
        "projects":        0.05,
        "flutter_bonus":   0.00,
    },
    "AI": {
        "leetcode":        0.25,
        "cf_rating":       0.05,
        "github_repos":    0.20,
        "projects":        0.50,
        "flutter_bonus":   0.00,
    },
}

# ── Internship-readiness thresholds ───────────────────────────────────────────
THRESHOLDS = {
    "AppDev": {"leetcode_min": 100, "projects_min": 1, "flutter_min": 1},
    "WebDev": {"leetcode_min": 80,  "projects_min": 1, "github_min": 5},
    "CP":     {"cf_min": 1400,      "leetcode_min": 200},
    "AI":     {"leetcode_min": 150, "projects_min": 1, "github_min": 4},
}


# ── Topic roadmap hints (deterministic lookup table) ──────────────────────────
TOPIC_HINTS = {
    "AppDev": ["State Management (BLoC/Provider)", "REST API integration", "Firebase Auth",
                "Flutter animations", "Unit & widget testing", "Play Store deployment"],
    "WebDev": ["React hooks & context", "REST + GraphQL APIs", "CSS Grid & Flexbox mastery",
                "Backend basics (Node.js / Django)", "Webpack & performance", "Deploy on Vercel/Netlify"],
    "CP":     ["Graph algorithms (Dijkstra, BFS/DFS)", "Dynamic Programming patterns",
                "Segment Trees & Fenwick Trees", "Modular arithmetic & combinatorics",
                "Participate in 3 Codeforces rounds/week", "Virtual contests on Atcoder"],
    "AI":     ["Scikit-learn pipelines", "PyTorch / TensorFlow basics", "EDA with Pandas & Matplotlib",
                "Kaggle competitions (top 20%)", "Deploy an ML model on HuggingFace Spaces",
                "Read 2 research papers / month"],
}


class CareerLogicEngine:
    """
    Core intelligence engine.  Everything is a pure function of the inputs —
    no randomness, no external calls, no LLM.
    """

    def __init__(self, profile: dict):
        self.profile = profile
        self.interest = profile["interest"]
        self.w = WEIGHTS[self.interest]

        # Derived helpers
        self.flutter_count = profile.get("flutter_projects", 0)
        self.has_flutter   = self.flutter_count > 0
        self.project_count = len(profile.get("projects", []))
        self.lc            = profile["leetcode"]
        self.cf            = profile["cf_rating"]
        self.github        = profile["github_repos"]
        self.year          = profile["year"]

    # ── 1. Normalization ──────────────────────────────────────────────────────
    def _norm(self, value, ceiling):
        return min(value / ceiling, 1.0)

    # ── 2. Weighted Scoring (the core math) ───────────────────────────────────
    def calculate_readiness(self) -> dict:
        """
        Returns a dict with:
          - score (0–100)
          - component_scores  (raw weighted contributions)
          - trace             (human-readable formula string)
        """
        w  = self.w
        lc_n   = self._norm(self.lc,            NORM["leetcode"])
        cf_n   = self._norm(self.cf,            NORM["cf_rating"])
        gh_n   = self._norm(self.github,        NORM["github"])
        pr_n   = self._norm(self.project_count, NORM["projects"])
        fl_n   = self._norm(self.flutter_count, 4)   # max 4 flutter projects

        components = {
            "LeetCode":         round(lc_n * w["leetcode"]        * 100, 2),
            "CF Rating":        round(cf_n * w["cf_rating"]        * 100, 2),
            "GitHub Repos":     round(gh_n * w["github_repos"]     * 100, 2),
            "Projects":         round(pr_n * w["projects"]         * 100, 2),
            "Flutter Bonus":    round(fl_n * w["flutter_bonus"]    * 100, 2),
        }

        score = round(sum(components.values()), 1)
        score = min(score, 100)   # cap at 100

        # Build the human-readable trace string
        trace_parts = []
        raw_values = {
            "LeetCode":      (self.lc,            NORM["leetcode"],  w["leetcode"]),
            "CF Rating":     (self.cf,            NORM["cf_rating"], w["cf_rating"]),
            "GitHub Repos":  (self.github,        NORM["github"],    w["github_repos"]),
            "Projects":      (self.project_count, NORM["projects"],  w["projects"]),
            "Flutter Bonus": (self.flutter_count, 4,                 w["flutter_bonus"]),
        }
        for label, (raw, ceil_, weight) in raw_values.items():
            norm_val = round(min(raw / ceil_, 1.0), 3)
            contrib  = round(norm_val * weight * 100, 2)
            trace_parts.append(
                f"({raw}/{ceil_}) × {weight} × 100 = {contrib}  [{label}]"
            )

        trace = " + ".join([f"{v:.2f}" for v in components.values()])
        trace += f" = {score}"

        return {
            "score":             score,
            "component_scores":  components,
            "trace_parts":       trace_parts,
            "formula_summary":   trace,
            "weights_used":      {k: v for k, v in w.items()},
        }

    # ── 3. Decision Tree → Career State ───────────────────────────────────────
    def diagnose_state(self) -> dict:
        """
        Deterministic rule-based router.
        Returns state label + the exact rule that fired.
        """
        lc   = self.lc
        cf   = self.cf
        yr   = self.year
        proj = self.project_count
        interest = self.interest

        # Rule set (evaluated in priority order — first match wins)
        if yr <= 2 and lc >= 350 and proj == 0:
            return {
                "state":  "ProjectRequired",
                "rule":   f"RULE: Year={yr}, LeetCode={lc}≥350, Projects=0 → You have strong DSA but NO project portfolio. Internships require both.",
                "emoji":  "⚠️",
                "color":  "warning",
            }

        if interest == "AppDev" and self.has_flutter and lc >= 100:
            return {
                "state":  "Ready",
                "rule":   f"RULE: Interest=AppDev AND hasFlutterProject=True AND LeetCode={lc}≥100 → Internship Ready.",
                "emoji":  "✅",
                "color":  "success",
            }

        if interest == "CP" and cf >= 1600:
            return {
                "state":  "Excellent",
                "rule":   f"RULE: Interest=CP AND CodeforcesRating={cf}≥1600 → Expert-level competitive programmer. Top-tier ready.",
                "emoji":  "🏆",
                "color":  "excellent",
            }

        if interest == "CP" and cf >= 1200 and lc >= 200:
            return {
                "state":  "OnTrack",
                "rule":   f"RULE: Interest=CP AND CF={cf}≥1200 AND LeetCode={lc}≥200 → On track. Push CF rating above 1600.",
                "emoji":  "📈",
                "color":  "info",
            }

        if interest == "WebDev" and proj >= 1 and self.github >= 5:
            return {
                "state":  "Ready",
                "rule":   f"RULE: Interest=WebDev AND Projects={proj}≥1 AND GitHub={self.github}≥5 → Internship Ready.",
                "emoji":  "✅",
                "color":  "success",
            }

        if interest == "AI" and proj >= 1 and lc >= 150:
            return {
                "state":  "Ready",
                "rule":   f"RULE: Interest=AI AND Projects={proj}≥1 AND LeetCode={lc}≥150 → Internship Ready.",
                "emoji":  "✅",
                "color":  "success",
            }

        if proj == 0:
            return {
                "state":  "ProjectRequired",
                "rule":   f"RULE: Projects=0 → No project portfolio. Build at least 1 complete project relevant to your interest.",
                "emoji":  "🚧",
                "color":  "warning",
            }

        # Score-based fallback
        score = self.calculate_readiness()["score"]
        if score >= 75:
            return {"state": "Excellent", "rule": f"RULE: Composite score={score}≥75 → Excellent profile.", "emoji": "🏆", "color": "excellent"}
        if score >= 55:
            return {"state": "OnTrack",   "rule": f"RULE: Composite score={score}≥55 → On track for internship season.",   "emoji": "📈", "color": "info"}
        return {
            "state": "SkillGap",
            "rule":  f"RULE: Composite score={score}<55 → Skill gap identified. Follow the roadmap below.",
            "emoji": "🔧",
            "color": "danger",
        }

    # ── 4. State Machine → Roadmap ────────────────────────────────────────────
    def generate_roadmap(self, state: str, peer_top_pct: float) -> list:
        """
        Returns a list of concrete, prioritised next-step strings.
        Generated entirely from state + profile data, with no LLM.
        """
        steps = []
        interest  = self.interest
        lc        = self.lc
        cf        = self.cf
        proj      = self.project_count
        github    = self.github

        # ── Universal rules ──────────────────────────
        if lc < 150:
            steps.append(f"🎯 Solve {150 - lc} more LeetCode problems to hit the 150 baseline (currently {lc}).")
        elif lc < 300:
            steps.append(f"🎯 Solve {300 - lc} more LeetCode problems to hit 300 (currently {lc}).")

        if proj == 0:
            steps.append("🚀 Build your FIRST complete project end-to-end and push it to GitHub with a README.")

        # ── Interest-specific rules ───────────────────
        if interest == "AppDev":
            if not self.has_flutter:
                steps.append("📱 Build at least 1 Flutter project — this is the top mobile stack for VJTI internships.")
            elif self.flutter_count < 2:
                steps.append("📱 Add a second Flutter project with Firebase backend to strengthen your portfolio.")
            if github < 8:
                steps.append(f"💻 Push more work to GitHub — aim for {8 - github} more repos (currently {github}).")
            steps.append("🔗 Integrate a public API (Maps / Weather / News) in your next app.")

        elif interest == "WebDev":
            if github < 10:
                steps.append(f"💻 Aim for 10+ GitHub repos. You have {github} — add {10 - github} more projects.")
            if proj < 2:
                steps.append("🌐 Build a Full-Stack project (React frontend + Django/Node backend + DB).")
            steps.append("⚡ Deploy one project on Vercel or Railway and add the live link to your resume.")

        elif interest == "CP":
            if cf < 1200:
                steps.append(f"⚔️ Participate in 3 Codeforces rounds this week — your rating is {cf}, target 1200+.")
            elif cf < 1600:
                steps.append(f"⚔️ CF Rating is {cf}. Solve Div.2 C/D problems daily to cross 1600 (Expert).")
            else:
                steps.append("⚔️ You're Expert+. Tackle Div.1 C problems and aim for 1900+ (Candidate Master).")
            if lc < 400:
                steps.append(f"🧩 Solve {400 - lc} more LeetCode Mediums/Hards (currently {lc}) for product company OAs.")

        elif interest == "AI":
            if proj < 2:
                steps.append("🤖 Build an end-to-end ML project: data → model → deployed API. Put it on GitHub.")
            if github < 8:
                steps.append(f"💻 Add {8 - github} more repos (notebooks, experiments, datasets) to your GitHub.")
            steps.append("📊 Enter a Kaggle competition and document your approach — top 25% impresses recruiters.")

        # ── Peer-based stretch goal ───────────────────
        if peer_top_pct > 20:
            steps.append(f"🏅 You're in the Top {round(peer_top_pct)}% of peers. Solve 20 more hard problems + 1 project to crack Top 10%.")
        elif peer_top_pct > 10:
            steps.append(f"🏅 Top {round(peer_top_pct)}% — you're close to Top 5%. Add one more impactful project to pull ahead.")

        # ── Generic topics from topic table ──────────────
        hints = TOPIC_HINTS.get(interest, [])
        for h in hints[:3]:
            steps.append(f"📚 Learn: {h}")

        steps.append("📄 Polish your resume: 1 page, showcase 2–3 best projects with impact numbers.")
        steps.append("🤝 DM 3 VJTI alumni on LinkedIn working in your interest area — ask for referrals.")

        return steps
