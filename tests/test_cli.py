import subprocess, json, sys
from pathlib import Path
def test_cli_scan_runs(tmp_path):
    out = tmp_path / 'out.json'
    cmd = [sys.executable, 'cli/scan.py', '--path', 'sample_project', '--output', str(out)]
    print('Running', cmd)
    subprocess.check_call(cmd)
    assert out.exists()
    data = json.loads(out.read_text())
    assert 'result' in data
