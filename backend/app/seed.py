from .db import engine, metadata
from .models import audits
conn = engine.connect()
conn.execute(audits.insert().values(repo_name='sample_project', summary='Seeded', score=85))
print('Seeded DB')
