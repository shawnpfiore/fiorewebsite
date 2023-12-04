"""
Django settings for fiore_website project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from typing import List

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, "fiore_website")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1eya)=-^suk0%&g@$zr8@_&nk@8sj@7)szl%^#w+9m3&t_q69t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: don't use a wildcard in production!
ALLOWED_HOSTS: List[str] = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fiore_website.apps.accounts',
    "fiore_website.apps.contact",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fiore_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fiore_website.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', default="")
POSTGRES_DB = os.environ.get('POSTGRES_DB', default="")
POSTGRES_USER = os.environ.get('POSTGRES_USER', default="")
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', default="")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_DB,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Django Dev Auth Settings
LOGIN_URL = "account:login"
LOGIN_REDIRECT_URL = "public:index"
LOGOUT_REDIRECT_URL = "public:index"

# Email settings
"""
EMAIL_HOST = "localhost"
EMAIL_PORT = "1025"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False
"""
# Django Prod Auth Settings
"""


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "shawnpfiore1978@gmail.com"
"""
LOGIN_URL = "account:login"
LOGIN_REDIRECT_URL = "public:index"
LOGOUT_REDIRECT_URL = "public:index"

# Email settings for gmail
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = "587"
EMAIL_HOST_USER = "shawnpfiore1978@gmail.com"
EMAIL_HOST_PASSWORD = "tyuhazkibiaepxpa"
DEFAULT_FROM_EMAIL = "shawnpfiore1978@gmail.com"
EMAIL_USE_TLS = True

# Email settings
# Website https://app-smtp.brevo.com/real-time
# Sign in with Google account below
"""
EMAIL_HOST = "smtp-relay.sendinblue.com"
EMAIL_PORT = "587"
EMAIL_HOST_USER = "shawnpfiore1978@gmail.com"
EMAIL_HOST_PASSWORD = "mNJfIQhAnWvj3Zdk"
DEFAULT_FROM_EMAIL = "sfiore@ecsorl.com"
EMAIL_USE_TLS = True
"""