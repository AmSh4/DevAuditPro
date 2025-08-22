# DevAuditPro

**DevAuditPro** — A recruiter-attractive full-stack developer tool for automated code auditing, CI integration, and developer productivity.  
Includes: FastAPI backend, React + Tailwind frontend, CLI scanner, SQLite storage, Docker, GitHub Actions, tests, sample datasets, and rich README & project structure.

## Highlights (what makes it stand out)
- Multi-file, multi-folder real project structure suitable for GitHub.
- Static code analyzer + heuristic ML training script (simple, explainable).
- Web dashboard to view scan results and historical trends.
- Docker + GitHub Actions for CI.
- Clear, production-like README, contributing guide, and license.

## Quick start (developer-friendly)
1. Backend (Python):
   - Create venv: `python -m venv .venv && source .venv/bin/activate`
   - Install: `pip install -r backend/requirements.txt`
   - Run: `uvicorn backend.main:app --reload --port 8000`

2. Frontend (React):
   - `cd frontend`
   - `npm install`
   - `npm run dev` (or `npm start`)

3. Run CLI scanner:
   - `python cli/scan.py --path ./sample_project --output results.json`

4. Or run with Docker:
   - `docker-compose up --build`

## Project structure
See `PROJECT_STRUCTURE.md` for a full tree.

## Files included
- backend/: FastAPI backend with SQLite and API for scans.
- frontend/: React + Tailwind app (Vite).
- cli/: Command-line scanner and trainer.
- sample_project/: Example repo to scan.
- docker/: Dockerfiles and docker-compose.
- .github/: GitHub Actions workflow to run scans on push.
- tests/: pytest tests for backend and CLI.

## Notes
- The ML/training script is lightweight and only used to demonstrate a data-driven feature; the analyzer works out-of-the-box using heuristics.
- Designed to be ready for recruiters: clean architecture, tests, CI, Docker, and UX.

Enjoy — modify and upload to GitHub as a ready portfolio project.
