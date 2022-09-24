from unicodedata import name
from django.urls import path
from apps.users.api.api import UserViewSet,MemberListAPIVIEW,SubcriptionsViewSet

from rest_framework.routers import DefaultRouter
from django.urls import path,include

from apps.products.api.views.product_viewset import *

router = DefaultRouter()

router.register(r"usuario",UserViewSet,basename="usuario")
router.register(r"subcripcion",SubcriptionsViewSet,basename="subcripcion")


urlpatterns = [
    path("usuario/membership/",MemberListAPIVIEW.as_view(),name="membership"),
    path("",include(router.urls))
]
