import os
from psycopg import connect
def get_db_connection():
    db_url = os.environ.get('DATABASE_URL')
    if db_url:
        return connect(db_url)
    else:
        print('Running in-memory database')
        return None
