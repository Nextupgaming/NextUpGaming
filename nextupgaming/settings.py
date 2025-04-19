import dj_database_url
import os

import os

TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
raw_db_url = os.environ.get("DATABASE_URL")
ROOT_URLCONF = 'nextupgaming.urls'
WSGI_APPLICATION = 'nextupgaming.wsgi.application'
if isinstance(raw_db_url, bytes):  # Decode if needed
    raw_db_url = raw_db_url.decode()
DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get("DATABASE_URL", "").decode("utf-8") if isinstance(os.environ.get("DATABASE_URL"), bytes) else str(os.environ.get("DATABASE_URL")),
        conn_max_age=600,
        ssl_require=True
    )
}
