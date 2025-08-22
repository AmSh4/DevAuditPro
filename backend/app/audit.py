import re
import json
from typing import List
from pathlib import Path

# Heuristic rules for scanning code
RULES = [
    ("Hardcoded password", r'(password\s*=\s*["\'].*["\'])'),
    ("Use of eval", r'\beval\('),
    ("Console log secrets", r'console\.log\(.*process\.env'),
    ("Potential SQL string concat", r'\+\s*".*SELECT|SELECT\s+.*\+'),
]

def scan_file(path: Path):
    issues = []
    try:
        text = path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return issues
    for name, pattern in RULES:
        if re.search(pattern, text):
            issues.append({"issue": name, "path": str(path)})
    # Simple complexity metric: lines > 200 flagged
    lines = text.count('\n') + 1
    if lines > 200:
        issues.append({"issue": "Large file (>200 lines)", "path": str(path), "lines": lines})
    return issues

def scan_repo(root: str):
    p = Path(root)
    results = []
    for f in p.rglob('*'):
        if f.is_file() and f.suffix in {'.py', '.js', '.ts'}:
            iss = scan_file(f)
            if iss:
                results.extend(iss)
    score = max(0, 100 - len(results)*5)
    summary = f'Found {len(results)} issues.'
    return {"summary": summary, "score": score, "issues": results}
