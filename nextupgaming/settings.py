import dj_database_url
import os
WSGI_APPLICATION = 'nextupgaming.wsgi.application'
DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}
