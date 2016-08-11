from .settings import *

DEBUG = True
SECRET_KEY = 42

INTERNAL_IPS = ['127.0.0.1']
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}


WEBPACK_STATS = os.path.join(BASE_DIR, 'static_build', 'webpack-stats-dev.json')
if os.path.exists(WEBPACK_STATS):
    WEBPACK_LOADER['DEFAULT']['STATS_FILE'] = WEBPACK_STATS
else:
    print("If you're editing frontend files, plase run `npm start` "
          "and restart Django.")
