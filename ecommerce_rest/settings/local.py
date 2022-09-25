from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
"""
DATABASES = {
    "default": {
        #"ENGINE": "django.db.backends.sqlite3",
        #"NAME": BASE_DIR /"db.sqlite3",
    },
    "users_db":{
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR /"users",
    },
    "products_db":{
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR /"products",
    }
}
"""
DATABASES = {
    "default": {},
    "users_db":{
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "d63rdosg4u4kn3",
        "USER":"donvggqseopnab",
        "PASSWORD":"0243b877918ca4499328c10389c44d2fc95a4baff11432b1d7d1141cee8f85d1",
        "HOST":"ec2-3-219-19-205.compute-1.amazonaws.com",
        "PORT":"5432"
    },
    "products_db":{
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "dff8e369o3h1nm",
        "USER":"lkhlemqiozmuzs",
        "PASSWORD":"b44299858eaf811a1a5b1595292b5e68784ab38359cf94a1510e2ba0ff59c56e",
        "HOST":"ec2-44-207-253-50.compute-1.amazonaws.com",
        "PORT":"5432"
    }
}




DATABASE_ROUTERS = ['database_routers.auth_router.AuthRouter',"database_routers.product_router.ProductRouter"]


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


