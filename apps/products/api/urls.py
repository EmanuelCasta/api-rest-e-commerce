from unicodedata import name
from django.urls import path
from apps.products.api.views.general_view import *
from apps.products.api.views.product_view import *

urlpatterns = [
    # Obtener todos los datos de cada uno de las caracteristicas de los productos
    path("size/",SizeListAPIView.as_view(),name="size"),
    path("business/",BusinessListAPIView.as_view(),name="business"),
    path("color/",ColorListAPIView.as_view(),name="color"),
    path("collection/",CollectionListAPIView.as_view(),name="collection"),
    path("indicator/",IndicatorListAPIView.as_view(),name="indicator"),
    path("sex/",SexListAPIView.as_view(),name="sex"),
    path("category/",CategoryListAPIView.as_view(),name="category"),
    path("country/",CountryListAPIView.as_view(),name="country"),
    path("reference/",ReferenceListAPIView.as_view(),name="reference"),

    #Obtener los productos
    path("product/information/",ProductListAPIView.as_view(),name="product"),
    path("product/sex/",Sex_BusinessListAPIView.as_view(),name="product/sex"),
    path("product/color/",Color_ProductAPIView.as_view(),name="product/color"),
    path("product/size/",Size_ProductListAPIView.as_view(),name="product/size"),
    path("product/business/sell/",Business_ProductListAPIView.as_view(),name="product/business"),
    path("product/business/sample/",Business_ProductShowListAPIView.as_view(),name="product/business"),

    
]