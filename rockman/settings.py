"""
Django settings for rockman project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import dj_database_url
from django.contrib import messages
from django_jinja.builtins import DEFAULT_EXTENSIONS
from rockman.processor import default

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir))

sys.path.insert(0, os.path.normpath(PROJECT_ROOT))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zn89yyf2ob_pc3bq)*y=swyqb)hv6$&ck(u9cj4!a0-pjc9sks'

DEBUG = True

DEBUG_TOOLBAR_PATCH_SETTINGS = DEBUG

TEMPLATE_DEBUG = DEBUG

MAINTENANCE = False

USE_L10N = True

USE_TZ = True

SITE_ID = 1

ROOT_URLCONF = 'rockman.urls'

WSGI_APPLICATION = 'rockman.wsgi.application'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'donotreply8386@gmail.com'
EMAIL_HOST_PASSWORD = 'password8386'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

ALLOWED_HOSTS = [
    '*.rockman.life',
]

INSTALLED_APPS = (
    'bootstrap3',
    'django_jinja',
    'django_admin_bootstrapped',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'debug_toolbar',
    
    # photologue apps
    'photologue',
    'sortedm2m',

    # zinna blog apps
    'rockman.blog',
    'zinnia_bootstrap',
    'django_comments',
    'mptt',
    'tagging',
    'zinnia',

    # rockman apps
    'rockman.base',
    'rockman.gallery',
    'rockman.todo',
    'rockman.meals',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///%s/rockman.sqlite' % PROJECT_ROOT)
}

# Static root is None because we don't want to collect static, we need
# to manage our own static files layout because the django package
# is bundled and will be located in site-packages
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

TEMPLATE_LOADERS = (
    'django_jinja.loaders.FileSystemLoader',
    'django_jinja.loaders.AppLoader',
    'app_namespace.Loader',
)

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja",
            "globals": {
                'get_messages': 'django.contrib.messages.api.get_messages',
            },
            "extensions": DEFAULT_EXTENSIONS + [
                'rockman.base.extensions.Django',
            ],
            "constants": default('')
        }
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                'django.core.context_processors.request',  # requires for zinnia
                'zinnia.context_processors.version',  # Optional for zinnia blog
                'rockman.processor.default',
            ],
        }
    },
]

try:
    from rockman.local_settings import *
except ImportError:
    pass
