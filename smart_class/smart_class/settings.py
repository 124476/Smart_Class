import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def load_bool(name, default):
    env_value = os.getenv(name, default=str(default)).lower()
    return env_value in ("true", "yes", "1", "y", "t", "on")


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SMART_CLASS_DJANGO_SECRET_KEY", default="no_key")

DEBUG = load_bool("SMART_CLASS_DJANGO_DEBUG", True)
DEFAULT_USER_IS_ACTIVE = load_bool("KANHUB_DJANGO_IS_ACTIVE", DEBUG)
MAX_AUTH_ATTEMPTS = int(
    os.getenv("SMART_CLASS_DJANGO_MAX_AUTH_ATTEMPTS", default=3),
)

ALLOWED_HOSTS = os.getenv("SMART_CLASS_DJANGO_ALLOWED_HOSTS", default="*").split(",")


INSTALLED_APPS = [
    "apps.users.apps.UsersConfig",
    "apps.homepage.apps.HomepageConfig",
    "apps.class_work.apps.ClassWorkConfig",
    "apps.api.apps.ApiConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tinymce",
    "active_link",
    "sorl.thumbnail",
    "rest_framework",
    "rest_framework.authtoken",
    "ckeditor",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.yandex",
]

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "width": "100%",
        "extraPlugins": "autogrow",
        "autoGrow_maxHeight": 500,
        "removePlugins": "resize",
        "placeholder": "Enter task description",
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "smart_class.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "smart_class.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation"
        ".UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        ".MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        ".CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        ".NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
    "apps.users.backends.AuthenticateBackend",
]

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static_dev"]
STATIC_ROOT = "static"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

LOGIN_URL = "/auth/login/"
LOGIN_REDIRECT_URL = "/auth/profile/"
LOGOUT_REDIRECT_URL = "/auth/login/"

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_CHANGE_EMAIL = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = "<[Smart Class]>"
SITE_ID = 1

EMAIL_HOST = os.getenv("SMART_CLASS_MAIL_HOST", default="smtp.mail.ru")
EMAIL_PORT = os.getenv("SMART_CLASS_MAIL_PORT", default=2525)
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = os.getenv(
    "SMART_CLASS_MAIL_USER",
    default="webmaster@localhost",
)
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
EMAIL_HOST_PASSWORD = os.getenv(
    "SMART_CLASS_MAIL_PASSWORD",
    default="secret_key",
)

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

SOCIALACCOUNT_PROVIDERS = {
    "yandex": {
        "APP": {
            "client_id": os.getenv(
                "SMART_CLASS_DJANGO_YANDEX_CLIENT_ID",
                default="apikey",
            ),
            "secret": os.getenv(
                "SMART_CLASS_DJANGO_YANDEX_SECRET",
                default="apikey",
            ),
            "key": "",
        },
        "SCOPE": [
            "login:info",
            "login:email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    },
}
