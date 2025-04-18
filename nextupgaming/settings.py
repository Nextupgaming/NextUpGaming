# settings placeholder
WSGI_APPLICATION = 'nextupgaming.wsgi.application'
import dj_database_url
import os

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}
