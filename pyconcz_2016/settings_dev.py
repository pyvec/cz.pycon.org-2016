from .settings import *

DEBUG = True
SECRET_KEY = 42

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pyconcz',
        'USER': 'pyconcz'
    }
}


def show_toolbar(request):
    return not request.is_ajax()


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}
DEBUG_TOOLBAR_PATCH_SETTINGS = False

if 'debug_toolbar' not in INSTALLED_APPS:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.insert(
        0, 'debug_toolbar.middleware.DebugToolbarMiddleware'
    )

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

WEBPACK_STATS = os.path.join(BASE_DIR, 'static_build', 'webpack-stats-dev.json')
if os.path.exists(WEBPACK_STATS):
    WEBPACK_LOADER['DEFAULT']['STATS_FILE'] = WEBPACK_STATS
else:
    print("If you're editing frontend files, plase run `npm start` "
          "and restart Django.")
