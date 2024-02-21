from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _
from . import  jazzmin

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-lo=l+$m@oc0_09e7fk$08#h#z-7ysuded#p!@jqor(8pdra9s9'


DEBUG = True

ALLOWED_HOSTS = []


DJANGO_APPS =[
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS =[
    'contact',
    'blog',
    'ckeditor',
    'about',
    'shop',
    'home',
    'pages',
    'regestration',
    
    

]



INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                
            ],
        },
    },
]


WSGI_APPLICATION = 'core.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation

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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


LANGUAGES = (
    ("uz", "Uzbek"),
    ("ru", "Russian"),
    ("en", "English"),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

LOCALE_PATHS = BASE_DIR / 'locale',




# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR / 'static'),
]


#  MEDIA FILES
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media/')



# Default primary key field type


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'








