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
gettext = lambda s: s # "To make your life easer" - http://docs.django-cms.org/en/release-3.3.x/how_to/install.html#configure-django-cms
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR)
PROJECT_BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# TODO: get from env variable
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b2j_&e=rzafa+zo874%tc^h!nbp#%0#442*19@(i&h-&s=v*hh'

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

LANGUAGES = [
    ('de', 'Deutsch')
]


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
    # TODO: 'reversion', - do we need this?
    # django cms plugins
    'djangocms_file',
    'djangocms_inherit',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'djangocms_link',
    # TODO: 'djangocms_snippet', - security hazard?
    'velafrica.cms_plugins.moneydonate',
    # custom apps
    'massadmin',
    'daterange_filter',
    'django_resized',
    'simple_history',
    'import_export',
    'django_object_actions',
    'rest_framework',
    'paypal.standard.ipn',
    # custom velafrica apps
    'velafrica.api',
    'velafrica.core',
    'velafrica.commission',
    'velafrica.counter',
    'velafrica.collection',
    'velafrica.download',
    'velafrica.frontend',
    'velafrica.organisation',
    'velafrica.stock',
    'velafrica.sbbtracking',
    #'velafrica.translation'
    'velafrica.transport',
    'velafrica.velafrica_sud',
    # django storages
    'storages',

    'webpack_loader',
)

# Django Storages Settings for SFTP


MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
)

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
)

SITE_ID = 1

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

# TODO: get from env variables, no passwords in code!
# Email settings
EMAIL_HOST = 'smtpauth.creta.ch'
EMAIL_HOST_USER = 'tracking@velafrica.ch'
EMAIL_HOST_PASSWORD = '!0q486ZjXeJilxfmwa#2HOc3PD5n1'
#EMAIL_PORT = 465
#EMAIL_USE_SSL = True

EMAIL_FROM_NAME = 'Velafrica Tracking'
EMAIL_FROM_EMAIL = 'tracking@velafrica.ch'


# TODO: get from env variables, no passwords in code!
# Django Storage settings
DEFAULT_FILE_STORAGE = 'storages.backends.ftp.FTPStorage'
FTP_STORAGE_LOCATION = 'ftp://nto5q-partnertoo:B1XqSY78ri0Vb94_hxws-C5nm6co@partnertool.velafrica.ch:21'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
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

PAYPAL_TEST = True

if 'PAYPAL_RECEIVER_MAIL' in os.environ:
    PAYPAL_RECEIVER_MAIL = os.environ['PAYPAL_RECEIVER_MAIL']
else:
    PAYPAL_RECEIVER_MAIL = ""
