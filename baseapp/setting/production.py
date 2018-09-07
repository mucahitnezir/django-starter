from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['your-domain.com']


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db-name',
        'USER': 'user-name',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')


# RECAPTCHA
# https://pypi.org/project/django-recaptcha/

RECAPTCHA_PUBLIC_KEY = 'prod-public-key'
RECAPTCHA_PRIVATE_KEY = 'prod-private-key'
NOCAPTCHA = True
RECAPTCHA_USE_SSL = True
