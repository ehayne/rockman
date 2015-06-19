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
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
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

WEB_HOST = '0.0.0.0'
WEB_PORT = '9005'
WEB_OPTIONS = {}

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

TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'app_namespace.Loader',
]

TEMPLATE_CONTEXT_PROCESSORS += (
  'django.core.context_processors.request',  # requires for zinnia
  'zinnia.context_processors.version',  # Optional for zinnia blog
  'rockman.processor.default',
)

# override tag name for bootstrap 3
MESSAGE_TAGS = {
    messages.SUCCESS: 'alert-success success',
    messages.WARNING: 'alert-warning warning',
    messages.ERROR: 'alert-danger error'
}

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

try:
    from rockman.local_settings import *
except ImportError:
    pass
