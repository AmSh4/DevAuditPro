# Simple trainer that demonstrates turning scan outputs into a CSV for ML.
# This is intentionally lightweight: it reads multiple stored JSON results and prepares features.
import json, csv, sys
from pathlib import Path

def build_csv(results_dir='training_data', out='training.csv'):
    Path(out).unlink(missing_ok=True)
    rows = []
    for p in Path(results_dir).glob('*.json'):
        d = json.loads(p.read_text())
        issues = d.get('result', {}).get('issues', [])
        row = {'repo': d.get('repo', p.stem), 'num_issues': len(issues)}
        rows.append(row)
    if not rows:
        print('No training data found in', results_dir)
        return
    keys = ['repo','num_issues']
    with open(out,'w',newline='') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(rows)
    print('Wrote', out)

if __name__ == '__main__':
    build_csv()
