import os
from pathlib import Path
from dotenv import load_dotenv
from decouple import config
from dj_database_url import parse as dburl
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-qw43jouzo_kilno^#iq9%!el$*z=snd@%p3fo)i@c^o463@2o7'

# トンネル起動時にngrokのURLを追加しないとログインできない
NGROK_URL = 'https://5d65-60-56-149-126.ngrok-free.app'
HEROKU_DEPLOY_URL = ""

DEBUG = True
# ALLOWED_HOSTS = [HEROKU_DEPLOY_URL, NGROK_URL, 'localhost', '127.0.0.1']
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [NGROK_URL]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "widget_tweaks",
    "app",
    "accounts",
    "line",
    "allauth",
    "allauth.account",
    "django.contrib.sites",
]

MIDDLEWARE = [
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"

# default_dburl = "sqlite:///" + str(BASE_DIR / "db.sqlite3")

# DATABASES = {
#     # "default": config("DATABASE_URL", default=default_dburl, cast=dburl),
#     'default': dj_database_url.config(default='postgres://localhost')
# }

default_dburl = "sqlite:///" + str(BASE_DIR / "db.sqlite3")

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL', default=default_dburl))
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ja"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = str(BASE_DIR / "staticfiles")

MEDIA_URL = "media/"
MEDIA_ROOT = str(BASE_DIR / "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SITE_ID = 1
LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_EMAIL_VERIFICATION = "none"
AUTH_USER_MODEL = "accounts.UserAccount"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False


# CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN")
# CHANNEL_SECRET = os.environ.get("CHANNEL_SECRET")
# LIFF_ID = os.environ.get("LIFF_ID")

CHANNEL_ACCESS_TOKEN="E3+3MMeFZoBbX/F1eVwDADjxntTTV+a0/FD9ioU7zj3vjecnSKXlxaumhxccgJQLwcnBkb0tdy7G7UWSJGXChMkjjg4eO1ENXvUR3cvEK4rTQiQ69/sFjneILNsqVQgk9Y+QqjUZIjh/geT9wKIxqQdB04t89/1O/w1cDnyilFU="
CHANNEL_SECRET="d982051de947fd76b0e12577604b2297"
LIFF_ID="2005226893-q0AxkgmP"

# デバッグ用の出力
print(f"CHANNEL_ACCESS_TOKEN: {CHANNEL_ACCESS_TOKEN}")
print(f"CHANNEL_SECRET: {CHANNEL_SECRET}")
print(f"LIFF_ID: {LIFF_ID}")
