# PathFinder

## Overview

Deterministic Career Readiness Analyzer is a web-based system that evaluates how prepared a computer science student is for software engineering internships. Unlike modern AI-powered tools that rely on large language models or external APIs, this system demonstrates **deterministic intelligence**—all reasoning and recommendations are generated through structured logic implemented directly in code.

The application analyzes measurable inputs such as coding practice, projects, competitions, and technical skills to generate a readiness score, identify skill gaps, and recommend actionable improvement steps. Every output is transparent and traceable to the input data and logic used by the system.

This project was developed for the **AI Without the API: Deterministic Intelligence Hackathon**, where the goal is to design intelligent systems without relying on runtime AI models.

---

## Problem Statement

Many students preparing for internships are unsure whether their current profile is strong enough. Existing tools often provide generic advice or opaque AI-generated feedback. Students need a system that:

* Evaluates their profile objectively
* Identifies missing skills
* Explains how decisions are made
* Provides a clear improvement roadmap

This project addresses that problem using deterministic logic.

---

## Key Features

### 1. Profile Evaluation Dashboard

Users enter factual information about their profile:

* Year of study
* LeetCode problems solved (Easy / Medium / Hard)
* Codeforces rating
* Number of projects and project complexity
* Hackathon participation and wins
* Technical skill areas
* Target career role (Software Engineer, App Developer, Competitive Programmer, etc.)

---

### 2. Weighted Scoring Engine

The system calculates internship readiness using a deterministic weighted scoring model.

Score Formula:

Score =
(Problem Solving × W1) +
(Project Strength × W2) +
(Competition Score × W3) +
(Skill Coverage × W4)

Weights change depending on the selected career role.

Example:

Software Engineer

* Problem Solving: 35%
* Projects: 40%
* Competitions: 15%
* Skills: 10%

Competitive Programmer

* Problem Solving: 60%
* Projects: 10%
* Competitions: 20%
* Skills: 10%

Problem-solving score is calculated using difficulty-based weighting.

Easy = 1 point
Medium = 3 points
Hard = 5 points

---

### 3. Rules Engine (Guidance System)

The application uses deterministic IF–THEN rules to generate improvement tasks.

Examples:

IF Year = 2 AND LeetCodeTotal < 200
→ Recommend solving foundational DSA problems.

IF TargetRole = App Developer AND Projects < 2
→ Recommend building a mobile or full-stack application.

IF Hackathons = 0
→ Recommend participating in at least one hackathon.

These rules create a personalized roadmap.

---

### 4. Decision Tree Diagnostic System

A rule-based diagnostic engine identifies the weakest areas in a student’s profile.

Example logic flow:

Start
→ Is ProblemSolvingScore below threshold?
→ Yes → Identify weakness in problem solving.

→ Are Projects below threshold?
→ Yes → Identify weakness in practical development.

→ Are Competitions low?
→ Yes → Identify lack of competitive exposure.

The system produces a **Skill Gap Report** ranked by severity.

---

### 5. Career Progression State Machine

The system models career readiness as a progression through defined stages.

States:

Explorer
Intermediate
Specialist
Placement Ready

Transitions occur only when deterministic requirements are met.

Example:

Explorer → Intermediate

* 100+ LeetCode problems
* At least 1 project

Intermediate → Specialist

* 300+ LeetCode problems
* 2 projects
* 1 hackathon

Specialist → Placement Ready

* 500+ LeetCode problems
* 3 projects
* 2 hackathons

---

### 6. Trajectory Prediction

The system estimates how long it will take a student to become internship-ready based on their learning pace.

Weekly Solve Rate =
Total Problems Solved / Weeks Active

Projected Readiness Time =
(Remaining Problems) / Weekly Solve Rate

This helps students understand how consistent effort affects their timeline.

---

### 7. Peer Comparison Engine

The application compares the user profile against benchmark profiles stored in a local dataset.

Example benchmark data:

* Average VJTI student profile
* Strong internship candidate profile

The system calculates the user's percentile ranking and displays relative performance.

Example output:

"You are in the top 20% compared to benchmark student profiles."

---

## Explainability Layer

One of the core design goals of this system is transparency.

Every result includes:

* Score breakdown
* Weight values used in calculations
* Rules triggered during evaluation
* Decision tree diagnostic path
* Career state explanation

This ensures that users can clearly understand how the system arrived at its conclusions.

---

## Technology Stack

Frontend

* HTML
* CSS
* JavaScript / React

Backend

* Node.js or Python Flask

Data Storage

* Local JSON files for benchmark profiles and rules

Processing

* All calculations performed locally without external APIs

---

## Hackathon Compliance

This project strictly follows the **AI Without the API** rules.

Allowed during development:

* AI tools for brainstorming
* AI coding assistance

Not used at runtime:

* Large Language Models
* Generative AI APIs
* Local LLM inference
* Non-deterministic model outputs

All intelligence is implemented through deterministic logic.

---

## System Architecture

User Input
↓
Scoring Engine
↓
Rules Engine
↓
Decision Tree Diagnostic
↓
State Machine Progression
↓
Explainability Layer
↓
User Dashboard Output

---

## Future Improvements

Possible extensions for future development include:

* Automatic GitHub profile analysis
* Real-time coding platform integrations
* More advanced benchmark datasets
* Dynamic skill graph visualization
* University-specific readiness benchmarks

---

## Conclusion

Deterministic Career Readiness Analyzer demonstrates how intelligent software systems can be built without relying on AI models. By combining structured scoring, rule-based reasoning, decision trees, and state machines, the system provides transparent and actionable career insights for students preparing for technical internships.
