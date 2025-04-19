from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
import dj_database_url
import os

import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'nextupgaming' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
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
        os.environ.get("DATABASE_URL", ""),
        conn_max_age=600,
        ssl_require=True
    )
}

    LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

TEMPLATES[0]['DIRS'] = [BASE_DIR / 'nextupgaming' / 'templates']
}
