from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '192.168.0.12', '127.0.0.1', 'localhost', 'mucahitnezir.pythonanywhere.com'
]


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')


# RECAPTCHA
# https://pypi.org/project/django-recaptcha/

RECAPTCHA_PUBLIC_KEY = '6LcjqmoUAAAAAHQCHCS9CrfkexuQi9JEdmry2dkn'
RECAPTCHA_PRIVATE_KEY = '6LcjqmoUAAAAAEP82lJFo03P_8mGx5CkPv5boUwq'
NOCAPTCHA = True
RECAPTCHA_USE_SSL = False
