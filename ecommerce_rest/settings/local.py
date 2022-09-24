from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Pasarela de pagos DEBUG
if DEBUG:
    STRIPE_PUBLISHABLE_KEY = ""
    STRIPE_SECRET_KEY = ""
else: 
    STRIPE_PUBLISHABLE_KEY = ""
    STRIPE_SECRET_KEY = ""



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"


