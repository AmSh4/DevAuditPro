from pathlib import Path
def sample_scan_run():
    # convenience: run a quick scan on sample_project included with repo
    from backend.app.audit import scan_repo
    res = scan_repo(str(Path(__file__).parents[1] / 'sample_project'))
    print(res)
