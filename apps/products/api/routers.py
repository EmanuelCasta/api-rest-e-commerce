from itertools import product
from rest_framework.routers import DefaultRouter
from django.urls import path,include

from apps.products.api.views.product_viewset import *

router = DefaultRouter()

router.register(r"product",ProductViewSetAPIView,basename="product")
router.register(r"sex_business",Sex_BusinessViewSetAPI,basename="sex_business")
router.register(r"color_product",Color_ProductViewSetAPI,basename="color_product")
router.register(r"business_product",Business_ProductViewSetAPI,basename="business_Product")
router.register(r"size_product",Size_ProductViewSetAPI,basename="Size_Product")



urlpatterns = [
    path('', include(router.urls)),
    path("representation_data/",Business_ProductShowViewSetAPI.as_view(),name="product_business"),
]