import os
from pathlib import Path
from dotenv import load_dotenv
from decouple import config
import dj_database_url

# .envファイルを読み込む
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'secret-key')

# トンネル起動時にngrokのURLを追加しないとログインできない
NGROK_URL = 'https://5d65-60-56-149-126.ngrok-free.app'
HEROKU_DEPLOY_URL = ""

DEBUG = config('DEBUG', default=True, cast=bool)
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

# デフォルトのSQLiteデータベースURL
default_dburl = "sqlite:///" + str(BASE_DIR / "db.sqlite3")

# DATABASE_URL環境変数が設定されている場合はPostgreSQLを使用し、設定されていない場合はSQLiteを使用
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

CHANNEL_ACCESS_TOKEN = config('CHANNEL_ACCESS_TOKEN', default='channel-access-token')
CHANNEL_SECRET = config('CHANNEL_SECRET', default='channel-secret')
LIFF_ID = config('LIFF_ID', default='liff-id')

# デバッグ用の出力
print(f"CHANNEL_ACCESS_TOKEN: {CHANNEL_ACCESS_TOKEN}")
print(f"CHANNEL_SECRET: {CHANNEL_SECRET}")
print(f"LIFF_ID: {LIFF_ID}")
