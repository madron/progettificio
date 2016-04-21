from .common import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# MIDDLEWARE_CLASSES.insert(0, 'cms.middleware.utils.ApphookReloadMiddleware')
