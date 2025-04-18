import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}
