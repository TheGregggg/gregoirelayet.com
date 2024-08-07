"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
import sys
from pathlib import Path

from typing_extensions import TypedDict

"""
------------------------------------
        Project settings
------------------------------------
"""

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.app"

# Application definition
APPS = ["apps.website", "apps.project", "apps.blog"]

THIRD_PARTY_APPS = [
    "django_htmx",
    "django_components",
    "django_components.safer_staticfiles",
    "whitenoise.runserver_nostatic",
    "pipeline",
]
WAGTAIL_APPS = [
    "wagtail.contrib.settings",
    "wagtail.sites",
    "wagtail_localize",
    "wagtail_localize.locales",
    "wagtail.contrib.redirects",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.images",
    "wagtail.documents",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "taggit",
    "modelcluster",
]

INSTALLED_APPS = (
    [
        "django.contrib.admin.apps.SimpleAdminConfig",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
    ]
    + APPS
    + THIRD_PARTY_APPS
    + WAGTAIL_APPS
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                        "django_components.template_loader.Loader",
                    ],
                )
            ],
            "builtins": [
                "django_components.templatetags.component_tags",
            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
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

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
# https://docs.wagtail.org/en/v6.0.5/advanced_topics/i18n.html
LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

WAGTAIL_I18N_ENABLED = True

WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ("fr", "French"),
    ("en", "English"),
]

# https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGE_COOKIE_AGE
LANGUAGE_COOKIE_NAME = "gl.com_lang"
LANGUAGE_COOKIE_HTTPONLY = False
LANGUAGE_COOKIE_AGE = 60 * 60 * 24 * 30  # 1 month


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "components"),
]
for apps in APPS:
    # apps = "apps.APP_NAME"
    STATICFILES_DIRS += [os.path.join(BASE_DIR, *apps.split("."), "components")]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# whitenoise
WHITENOISE_SKIP_COMPRESS_EXTENSIONS = (
    "jpg",
    "jpeg",
    "png",
    "gif",
    "webp",
    "avif",
    "zip",
    "gz",
    "tgz",
    "bz2",
    "tbz",
    "xz",
    "br",
    "swf",
    "flv",
    "woff",
    "woff2",
)
WHITENOISE_KEEP_ONLY_HASHED_FILES = True
WHITENOISE_USE_FINDERS = False


PIPELINE = {
    "STYLESHEETS": {
        "main": {
            "source_filenames": (
                "app.css",
                "*/website.css",
                "*/project.css",
                "*/blog.css",
                "*/style.css",
            ),
            "output_filename": "css/main.css",
        }
    },
    "JAVASCRIPT": {
        "components": {
            "source_filenames": ("*/script.js",),
            "output_filename": "js/components.js",
        }
    },
    "CSS_COMPRESSOR": "pipeline.compressors.csshtmljsminify.CssHtmlJsMinifyCompressor",
    "JS_COMPRESSOR": "pipeline.compressors.csshtmljsminify.CssHtmlJsMinifyCompressor",
    "DISABLE_WRAPPER": True,
}


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# Django components
COMPONENTS = {
    "context_behavior": "django",
}


# WAGTAIL
WAGTAIL_SITE_NAME = "Greg's website"
TAGGIT_CASE_INSENSITIVE = True

WAGTAILADMIN_BASE_URL = "gregadmin"


"""
------------------------------------
        Instance settings
------------------------------------
"""

TESTING = "test" in sys.argv

SECRET_KEY = "this_is_not_secret"

# Database
DB_Options_Typing = TypedDict("DB_Options_Typing", {"options": str})
DB_Test_Typing = TypedDict("DB_Test_Typing", {"OPTIONS": DB_Options_Typing})
DB_Typing = TypedDict(
    "DB_Typing",
    {
        "ENGINE": str,
        "NAME": str,
        "USER": str,
        "PASSWORD": str,
        "HOST": str,
        "PORT": str,
        "OPTIONS": DB_Options_Typing,
        "TEST": DB_Test_Typing,
    },
)


DATABASES: dict[str, DB_Typing] = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "gregoirelayet.com",
        "USER": "gerg",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "PORT": "5432",
        "OPTIONS": {
            "options": "-c search_path=gregoirelayet.com.schema",
        },
        "TEST": {
            "OPTIONS": {
                "options": "-c search_path=test_gregoirelayet.com.schema",
            },
        },
    }
}


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    },
}
