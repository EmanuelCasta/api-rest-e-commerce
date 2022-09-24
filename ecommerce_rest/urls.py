"""ecommerce_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)

from apps.users.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("usuario/",include("apps.users.api.urls")),
    path('logout/', Logout.as_view(), name='Logout'),# Sirve para refrescar el token que sirven para acceder 
    path('login/', Login.as_view(), name='Login'),# retornar el token de acceso y el token de refresco de cada usuario
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),# retornar el token de acceso y el token de refresco de cada usuario
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),# Sirve para refrescar el token que sirven para acceder 
    #path("products-nike-webScraping/",include("apps.products.api.urls")),
    path("products_nike/",include("apps.products.api.routers")),
    path("products-puma/",include("apps.products.api.urls")),
]
