from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database api-rest

DATABASES = {
    "default": {
        #"ENGINE": "django.db.backends.sqlite3",
        #"NAME": BASE_DIR /"db.sqlite3",
    },
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
        "NAME": "products",
        "USER":"",
        "PASSWORD":"",
        "HOST":"",
        "PORT":""
    }
}

DATABASE_ROUTERS = ['database_routers.auth_router.AuthRouter',"database_routers.product_router.ProductRouter"]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

