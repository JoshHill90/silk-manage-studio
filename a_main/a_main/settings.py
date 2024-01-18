from pathlib import Path
from dotenv import load_dotenv
import os
from decouple import config
from .env.app_Logic.KeyPass import SETTINGS_KEYS
load_dotenv()
#-------------------------------------------------------------------------------------------------------#
# dev env settings 
#-------------------------------------------------------------------------------------------------------#

BASE_DIR = Path(__file__).resolve().parent.parent
get_value = SETTINGS_KEYS

#-------------------------------------------------------------------------------------------------------#
# Project settings
#-------------------------------------------------------------------------------------------------------#

SECRET_KEY = get_value.DJANGO_KEY

DEBUG = True

#ALLOWED_HOSTS = ['test-site-2.silkthreaddev.com', 'www.test-site-2.silkthreaddev.com']
ALLOWED_HOSTS = []

#-------------------------------------------------------------------------------------------------------#
# Base Directory setup
#-------------------------------------------------------------------------------------------------------#


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'bootstrap5',
    'ckeditor',
    'client',
    'gallery',
    'site_app',
    'logs',
    'user'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = ['https://test-site-2.silkthreaddev.com']
ROOT_URLCONF = 'a_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'a_main.wsgi.application'


#-------------------------------------------------------------------------------------------------------#
# Database and Autherization
#-------------------------------------------------------------------------------------------------------#

DATABASES = {
  'default': {
    'ENGINE': 'django_psdb_engine',
    'NAME': get_value.DB_NAME,
    'HOST': get_value.DB_HOST,
    'PORT': get_value.DB_PORT,
    'USER': get_value.DB_USER,
    'PASSWORD': get_value.DB_PASSWORD,
    'OPTIONS': {'ssl': {'ssl-ca': get_value.MYSQL_ATTR_SSL_CA}, 'charset': 'utf8mb4'}
  } 
}
#-------------------------------------------------------------------------------------------------------#
# Password validation
#-------------------------------------------------------------------------------------------------------#

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

#-------------------------------------------------------------------------------------------------------#
# Time-zone/Language  
#-------------------------------------------------------------------------------------------------------#

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

#-------------------------------------------------------------------------------------------------------#
# Directory and URLS 
#-------------------------------------------------------------------------------------------------------#
STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
LOGIN_REDIRECT_URL = 'o-gallery'
LOGOUT_REDIRECT_URL = 'o-gallery'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# HTTPSS Settings 
SESSION_COOKI_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = False

# HSTS Settings
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
