from .base import *


ALLOWED_HOSTS = ['*']



""" Place the Production database configuration here. """

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
