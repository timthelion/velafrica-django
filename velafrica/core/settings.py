# -*- coding: utf-8 -*-
"""
Django settings for velafrica_trackingtool project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

gettext = lambda \
        s: s  # "To make your life easer" - http://docs.django-cms.org/en/release-3.3.x/how_to/install.html#configure-django-cms
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR)
PROJECT_BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
if 'DEBUG' in os.environ:
    if os.environ['DEBUG'] == 'True':
        DEBUG = True
    else:
        DEBUG = False
else:
    DEBUG = False

INTERNAL_IPS = (
    '127.0.0.1',
)

# TODO: define for production
ALLOWED_HOSTS = ['*']

LANGUAGES_CODE = 'de-ch'

LANGUAGES = [
    ('de', 'Deutsch'),
    ('en', 'English'),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "velafrica/frontend/locale"),
)

# Application definition
INSTALLED_APPS = (
    # autocomplete light
    'dal',
    'dal_select2',
    # django core apps
    'django.contrib.contenttypes',
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # django cms
    'cms',  # django CMS itself
    'djangocms_text_ckeditor',
    'treebeard',  # utilities for implementing a tree
    'menus',  # helper for model independent hierarchical website navigation
    'sekizai',  # for JavaScript and CSS management
    'easy_thumbnails',
    'filer',
    'aldryn_apphooks_config',
    'cmsplugin_filer_image',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',
    'djangocms_blog',
    # django cms plugins
    'djangocms_file',
    'djangocms_inherit',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'djangocms_link',
    # custom django cms plugins
    'velafrica.cms_plugins.big_picture',
    'velafrica.cms_plugins.row',
    # custom apps
    'massadmin',
    'daterange_filter',
    'django_resized',
    'simple_history',
    'import_export',
    'django_object_actions',
    'django_filters',
    'paypal.standard.ipn',
    # restframework
    'rest_framework',
    'corsheaders',
    'rest_framework_swagger',
    # custom velafrica apps
    'velafrica.api',
    'velafrica.core',
    # 'velafrica.commission', just a PoC, not used in production
    'velafrica.counter',
    'velafrica.collection',
    'velafrica.download',
    'velafrica.frontend',
    'velafrica.organisation',
    'velafrica.public_site',
    'velafrica.stock',
    'velafrica.sbbtracking',
    # 'velafrica.translation'
    'velafrica.transport',
    'velafrica.velafrica_sud',
    # django storages
    'storages',

    'webpack_loader',
    'mailchimp',
)

MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'velafrica.core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'frontend/templates/')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

CMS_TEMPLATES = (
    ('cms/base.html', 'Base'),
    ('cms/base.html', 'Base'),
)

# Settings for Blog
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
META_SITE_PROTOCOL = 'http'
META_USE_SITES = True

PARLER_LANGUAGES = {
    1: (
        {'code': 'de'},
    ),
    'default': {
        'fallbacks': ['de'],
    }
}

WSGI_APPLICATION = 'velafrica.core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

import dj_database_url

DATABASES = {
    'default': dj_database_url.config()
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'de'

# list of time zones https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIME_ZONE = 'Europe/Zurich'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/auth/login'
LOGIN_REDIRECT_URL = '/auth/profile'
LOGOUT_URL = '/auth/logout'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(PROJECT_BASE_DIR, 'staticfiles', 'dist'),
)

# Media files (Files uploaded by user)

MEDIA_URL = 'http://partnertool.velafrica.ch/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, "media")

# Django Resized
DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True

# Email settings
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_USE_SSL = True

EMAIL_FROM_NAME = 'Velafrica Tracking'
EMAIL_FROM_EMAIL = 'tracking@velafrica.ch'

# Django Storage settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_SECURE_URLS = False
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_CUSTOM_DOMAIN = os.environ['AWS_S3_CUSTOM_DOMAIN']

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination'
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'build/' if DEBUG else 'dist/',
        'STATS_FILE': os.path.join(
            PROJECT_BASE_DIR,
            'tmp',
            'webpack-stats.json' if DEBUG else 'webpack-stats-prod.json',
        ),
        'POLL_DELAY': 0.2,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    },
}

ROLLBAR = {
    'access_token': '',
    'environment': 'development' if DEBUG else 'production',
    'branch': 'master',
    'root': '/app',
}
if 'ROLLBAR_ACCESS_TOKEN' in os.environ:
    ROLLBAR['access_token'] = os.environ['ROLLBAR_ACCESS_TOKEN']

if 'PAYPAL_TEST' in os.environ:
    if os.environ['PAYPAL_TEST'] == 'True':
        PAYPAL_TEST = True
    else:
        PAYPAL_TEST = False
else:
    PAYPAL_TEST = False

PAYPAL_RECEIVER_MAIL = os.environ['PAYPAL_RECEIVER_MAIL']
GMAP_API_KEY = os.environ['GMAP_API_KEY']

# Due to a mistake the SITE_ID on staging has to be 2 but will be 1 on production
# so its configurable per env variable (shame on HaRii)
if 'SITE_ID' in os.environ:
    SITE_ID = int(os.environ['SITE_ID'])
else:
    SITE_ID = 1

MAILCHIMP_API_KEY = os.environ['MAILCHIMP_API_KEY']
MAILCHIMP_LIST_ID = os.environ['MAILCHIMP_LIST_ID']
ORDER_RECEIVER = os.environ['ORDER_RECEIVER']
INITIAL_VELO_COUNT = int(os.environ['INITIAL_VELO_COUNT'])
AVERAGE_VELOS_PER_DAY = int(os.environ['AVERAGE_VELOS_PER_DAY'])
FACEBOOK_APP_ID = os.environ['FACEBOOK_APP_ID']
