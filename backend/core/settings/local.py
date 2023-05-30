from .base_settings import *





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'Ecommerce',
#         'USER': 'postgres',
#         'PASSWORD': 'araa23o385',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
