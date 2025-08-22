from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AuditCreate(BaseModel):
    repo_name: str
    summary: str
    score: int

class Audit(BaseModel):
    id: int
    repo_name: str
    summary: str
    score: int
    created_at: datetime

    class Config:
        orm_mode = True
