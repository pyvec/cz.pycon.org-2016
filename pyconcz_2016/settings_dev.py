from .settings import *

DEBUG = True
SECRET_KEY = 42

INTERNAL_IPS = ['127.0.0.1']
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pyconcz',
        'USER': 'pyconcz',
        'PASSWORD': 'pyconcz',
        'HOST': 'db',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
