from sqlalchemy import Table, Column, Integer, String, Text, DateTime, MetaData
from sqlalchemy.sql import func
from .db import metadata

audits = Table(
    "audits",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("repo_name", String, index=True),
    Column("summary", Text),
    Column("score", Integer),
    Column("created_at", DateTime, server_default=func.now())
)
