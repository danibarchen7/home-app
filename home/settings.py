"""
Django settings for home project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""



from pathlib import Path
import os
from datetime import timedelta
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=os.environ.get('SECRET_KEY')
# SECRET_KEY = 'django-insecure-7b3_q(4mj&3xpt!@jsf+7o4_s(mzhunt45)l%#8#c4_5ye2vjg'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get("DEBUG","False").lower()=="true"
DEBUG = False
# ALLOWED_HOSTS=os.environ.get("ALLOWED_HOSTS").split(" ")
ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = 'Customer.Customers'

# Application definition

INSTALLED_APPS = [
    # 'channels',
    "daphne",
    'django.contrib.admin',
    'chat',
   
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # 'rest_framework_simplejwt',
    'rest_framework',
    'rest_framework.authtoken',
    # 'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'dj_rest_auth.registration',
    'corsheaders',
    # 'socketcluster_client',
    # 
    
    # 'channels_redis',
    'pusher',
    'Customer',
    'Comments',
    'Cure',
    'Favorites',
    'Images',
    'Property',
    'Type',
    
]



MIDDLEWARE = [
    
    # 'home.tokenauth_middleware.TokenAuthMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'channels.routing.ProtocolTypeRouter',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'rest_framework.authentication.TokenAuthentication',
    # 'channels.middleware.ChannelsMiddleware',
    # 'chatroom.middleware.ChatroomUserMiddleware',
    
    
    'allauth.account.middleware.AccountMiddleware'
]

# ASGI_APPLICATION = 'home.routing.application'


# SESAME_MAX_AGE = 30
ASGI_APPLICATION = "home.asgi.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
        # 'CONFIG': {
        #     'hosts': [('redis://localhost:6379')],
        # },
    },
}
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [('0.0.0.0', 8001)],
#             "hosts": [('0.0.0.0', 6379)],
#         },
#     },
# }

# Application settings

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#         ],
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication', ]
# }
AUTHENTICATION_CLASSES = [
    'rest_framework.authentication.SessionAuthentication',
]
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
}
# REST_FRAMEWORK = {
    
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     )
# }

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
#     'REFRESH_TOKEN_LIFETIME': timedelta(weeks=1),
#     'AUTH_HEADER_TYPES':('Bearer',)
# }
    
   

ROOT_URLCONF = 'home.urls'

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

# WSGI_APPLICATION = 'home.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#         # "TEST": {
#         #     "NAME": BASE_DIR / "db.sqlite3",
#         # },
#     }
# }
# DATABASE['default']=dj_database_url.parse("postgres://home_app_database_user:n2GGUICCdiiWIl9boUVoe0RKcG7EtHYw@dpg-cobb54q1hbls73apu80g-a/home_app_database    ")
# Replace the SQLite DATABASES configuration with PostgreSQL:
DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgres://home_app_database_user:n2GGUICCdiiWIl9boUVoe0RKcG7EtHYw@dpg-cobb54q1hbls73apu80g-a/home_app_database',
        conn_max_age=600
    )
}
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# reset password settings 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'danibarchene@gmail.com'
EMAIL_HOST_PASSWORD = 'ffrz peaf rtmx exyk'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOW_ALL_ORIGINS = True



# import keras
# import numpy as np
# from keras import backend as K
# import tensorflow as tf
# from tensorflow.python.keras.backend import set_session
# from keras.applications import vgg16


# def get_session():
#     config = tf.config.experimental.list_physical_devices('GPU')
#     tf.config.experimental.set_memory_growth(config, True)
#     return tf.Session(config=config)

# K.set_session(get_session())

# config = tf.config.experimental.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(config, True)
# SESS = tf.Session(config=config)
# print("model loading")
# GRAPH1 = tf.get_default_graph()

# set_session(SESS)
# # Load the VGG model
# VGG_MODEL = vgg16.VGG16(weights="imagenet")
