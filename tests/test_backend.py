from backend.app.main import app
from fastapi.testclient import TestClient
import os
client = TestClient(app)

def test_list_audits_empty_or_ok():
    res = client.get('/audits/')
    assert res.status_code == 200

def test_scan_missing_path():
    res = client.post('/scan/?repo_name=test&path=/not/exist')
    assert res.status_code == 400
