# PathFinder VJTI — Career Architect

Welcome to **PathFinder VJTI**, a deterministic, LLM-free career guidance web application purpose-built for VJTI Computer Engineering students. This project aims to assess student profiles, identify skill gaps, and provide actionable, personalized roadmaps—all backed by a completely transparent, logic-driven engine.

## 🎥 Demo

Check out the video demonstration of the application here:
[**Watch on YouTube**](https://youtu.be/oYcFEpp28S0)

---

## 🏗️ Architecture & Core Components

PathFinder built on a robust Django backend, utilizing vanilla HTML, CSS, and JS for its frontend. What sets it apart is its **100% Deterministic Logic Engine**. No unpredictable LLMs are used; every suggestion, score, and state diagnosis is traceably computed.

### 1. Career Logic Engine (`career/engine/career_logic_engine.py`)
This is the "brain" of the application. It takes a student's profile (containing metrics like LeetCode count, Codeforces rating, GitHub repositories, and projects) and processes it through carefully calibrated stages:

*   **Normalization:** Raw metrics are mapped to a 0–1 scale against predefined ceilings (e.g., Codeforces grandmaster at 2400, 700 LeetCode problems).
*   **Weighted Scoring:** Based on the chosen domain of interest (App Development, Web Development, Competitive Programming, or AI), a tailored set of weights is applied to the normalized scores to calculate an overall Readiness Score out of 100.
    *   *Example:* For Competitive Programming, Codeforces rating carries a massive 70% weight, whereas for Web Development, projects and GitHub repositories are prioritized.
*   **Decision Tree Diagnosis:** A rule-based router evaluates the profile metrics and readiness score to deterministically assign a state label: `Ready`, `Excellent`, `OnTrack`, `ProjectRequired`, or `SkillGap`—complete with the exact logic rule that fired.
*   **State Machine Roadmap Generator:** Depending on the diagnosed state and the domain, the engine conditionally generates a prioritized list of next steps, integrating both universal rules and interest-specific guidance.

### 2. Peer Ranking Engine (`career/engine/ranking_engine.py`)
To give students a realistic perspective on where they stand, the ranking engine calculates percentiles based on a curated peer dataset. It contextualizes a student's score relative to their peers from the same academic year and domain interest. 

### 3. Explainable UI
The frontend doesn't just show a final score; it acts as an **Explainable UI**. It visualizes the underlying logic through "traces"—showing the precise formula, normalization ceilings, and weight distributions that led to the final assessment, fostering trust and clarity.

## ⚙️ Tech Stack

*   **Backend:** Python, Django
*   **Database:** SQLite3 (development)
*   **Frontend:** HTML5, CSS3, Vanilla JavaScript
*   **Logic:** Pure Python deterministic rule engines

## 🚀 Getting Started

### Prerequisites
*   Python 3.8+
*   pip

### Installation & Execution

1.  **Clone the repository** (if not already done).
2.  **Navigate to the project directory:**
    ```bash
    cd PathFinder_vjti
    ```
3.  **Apply migrations** (optional if already applied):
    ```bash
    python manage.py migrate
    ```
4.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
5.  **Access the application** by navigating to `http://127.0.0.1:8000/` in your browser.

## 🤝 Contributing

Contributions are welcome! If you're a VJTI student and want to refine the domain weights, add new roadmap templates, or tackle UI enhancements, feel free to submit a pull request.