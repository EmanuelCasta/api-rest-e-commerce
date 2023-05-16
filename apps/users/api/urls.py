from unicodedata import name
from django.urls import path
from apps.users.api.api import UserViewSet,MemberListAPIVIEW,SubcriptionsViewSet,UserRegisterViewSet

from rest_framework.routers import DefaultRouter
from django.urls import path,include

from apps.products.api.views.product_viewset import *

router = DefaultRouter()

router.register(r"account",UserViewSet,basename="usuario")
router.register(r"register",UserRegisterViewSet,basename="register")
router.register(r"subcripcion",SubcriptionsViewSet,basename="subcripcion")


urlpatterns = [
    path("membership/",MemberListAPIVIEW.as_view(),name="membership"),
    path("",include(router.urls))
]
