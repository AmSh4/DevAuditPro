# DevAuditPro

**DevAuditPro** — A full-stack developer tool for automated code auditing, CI integration, and developer productivity. 

## Highlights
- Multi-file, multi-folder real project structure suitable for GitHub.
- Static code analyzer + heuristic ML training script (simple, explainable).
- Web dashboard to view scan results and historical trends.
- Docker + GitHub Actions for CI.

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

