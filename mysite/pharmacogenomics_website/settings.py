"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from dotenv import load_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env_path = os.path.join(BASE_DIR, 'pharmacogenomics.env')
load_dotenv(env_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ugbnazv9chk*!1d2mfs(&w#beok=wqa%h_i8f&l_es=exl+u*n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]



# Application definition

INSTALLED_APPS = [
    'pharmacogenomics.apps.PharmacogenomicsConfig',
    'gtexome.apps.GtexomeConfig',
    'metabolites.apps.MetabolitesConfig',
    'precursors.apps.PrecursorsConfig',
    'precursor_metabolite_map.apps.PrecursorMetaboliteMapConfig',
    'drug_name_precursor_map.apps.DrugNamePrecursorMapConfig',
    'full_metabolite_map.apps.FullMetaboliteMapConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
DCS_SESSION_COOKIE_SAMESITE = 'None'
DCS_SESSION_COOKIE_SAMESITE_FORCE_ALL = True

MIDDLEWARE_CLASSES = [
    'django_cookies_samesite.middleware.CookiesSameSite',
]

ROOT_URLCONF = 'pharmacogenomics_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'error.log',
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'info.log',
        }
    },
    'loggers': {
        'django.error': {
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.info': {
            'handlers': ['info'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

WSGI_APPLICATION = 'pharmacogenomics_website.wsgi.application'

BOOTSTRAP3 = {'include_jquery': True}


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

NAME = os.getenv('NAME')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': PORT,
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)

STATIC_URL = '/static/'
