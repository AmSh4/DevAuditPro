from fastapi import FastAPI, HTTPException
from .db import engine, metadata, SessionLocal
from . import models, audit, schemas
from sqlalchemy import select, insert
import os

metadata.create_all(bind=engine)

app = FastAPI(title='DevAuditPro API')

@app.post('/scan/')
def create_scan(repo_name: str, path: str):
    if not os.path.exists(path):
        raise HTTPException(status_code=400, detail='Path not found')
    result = audit.scan_repo(path)
    # save to DB
    with SessionLocal() as db:
        stmt = insert(models.audits).values(repo_name=repo_name, summary=result['summary'], score=result['score'])
        db.execute(stmt)
        db.commit()
    return result

@app.get('/audits/')
def list_audits():
    with SessionLocal() as db:
        res = db.execute(select(models.audits)).fetchall()
        rows = [dict(r) for r in res]
    return rows
