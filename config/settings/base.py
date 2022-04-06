

from pathlib import Path
import os

import environ
env = environ.Env()


BASE_DIR = Path(__file__).resolve().parent.parent.parent

environ.Env.read_env(BASE_DIR,'.env')

SECRET_KEY = env('SECRET_KEY')




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'blog',
    #third party
    'ckeditor',
    'crispy_forms',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'




# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'account.CustomUserModel'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL='/'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS=True
EMAIL_PORT=587
DEFAUL_FROM_EMAIL = 'yskizilay5858@gmail.com'
EMAIL_HOST_USER = 'yskizilay5858@gmail.com'
EMAIL_HOST_PASSWORD= env('EMAIL_PASSWORD')

LOGGING = {
    'version': 1,
    'disable_existing_loggers ': False,
    'formatters': {
        'basit_ifade': {
            'format': '{asctime} {levelname} {message} {name}',
            'style': '{'
        }
    },
    'handlers':{
        'console':{
            'class':'logging.StreamHandler'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/konu_okuma.log',
            'formatter': 'basit_ifade'
        }
    },
    'loggers':{
        'konu_okuma':{
            'handlers':['console', 'file'],
            'level':'INFO'
        }
    }
}