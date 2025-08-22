#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
from backend.app.audit import scan_repo

def main():
    p = argparse.ArgumentParser(description='DevAuditPro CLI scanner')
    p.add_argument('--path', required=True, help='Path to repository to scan')
    p.add_argument('--output', required=False, help='Write JSON output to file')
    p.add_argument('--repo', required=False, default='local-repo', help='Repo name')
    args = p.parse_args()
    res = scan_repo(args.path)
    out = {'repo': args.repo, 'result': res}
    if args.output:
        Path(args.output).write_text(json.dumps(out, indent=2))
        print(f"Results written to {args.output}")
    else:
        print(json.dumps(out, indent=2))

if __name__ == '__main__':
    main()
