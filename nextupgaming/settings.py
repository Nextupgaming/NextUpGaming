import dj_database_url
import os

raw_db_url = os.environ.get("DATABASE_URL")

if isinstance(raw_db_url, bytes):  # Decode if needed
    raw_db_url = raw_db_url.decode()

DATABASES = {
    'default': dj_database_url.parse(
        raw_db_url,
        conn_max_age=600,
        ssl_require=True
    )
}
