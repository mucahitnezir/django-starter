import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables
env = environ.Env()
env_file = os.path.join(BASE_DIR, '.env')
if os.path.isfile(env_file):
    env.read_env(env_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', [])

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('PSQL_DB_NAME'),
        'USER': env.str('PSQL_DB_USER'),
        'PASSWORD': env.str('PSQL_DB_PASSWORD'),
        'HOST': env.str('PSQL_DB_HOST', 'localhost'),
        'PORT': env.str('PSQL_DB_PORT', '5432')
    }
}

# Application definition
INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Myself
    'post',
    'category',
    'portfolio',
    'service',
    'setting',
    'home',
    'about',
    # Third
    'crispy_forms',
    'django_cleanup',
    'ckeditor',
    'captcha',
    'import_export',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.context_processors.parameters',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('tr', 'Turkish')
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/assets/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'node_modules')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# CRISPY
# https://django-crispy-forms.readthedocs.io/en/latest/index.html

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# CKEditor
# https://pypi.org/project/django-ckeditor/

CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%'
    }
}

# RECAPTCHA
# https://pypi.org/project/django-recaptcha/

RECAPTCHA_PUBLIC_KEY = env.str('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = env.str('RECAPTCHA_PRIVATE_KEY')
NOCAPTCHA = True
RECAPTCHA_USE_SSL = not DEBUG


# URLs

LOGIN_URL = 'account:login'
LOGOUT_URL = 'account:logout'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'account:login'


# Email
# https://docs.djangoproject.com/en/2.2/topics/email/#topic-email-backends

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = env.str('SENDGRID_API_KEY')
DEFAULT_FROM_EMAIL = env.str('DEFAULT_FROM_EMAIL', 'Awesome Company <info@example.com>')
