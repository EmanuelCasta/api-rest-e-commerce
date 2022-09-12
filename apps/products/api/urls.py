from unicodedata import name
from django.urls import path
from apps.products.api.views.general_view import *
from apps.products.api.views.product_view import *

urlpatterns = [

    

    # Listar los productos
    path("list/product/business/sample/",Business_ProductShowListAPIView.as_view(),name="product_business"),

    #Crear Productos o listar 
    path("product/",ProductListCreateAPIView.as_view(),name="product_business"),
    path("product/sex/",Sex_BusinessListCreateAPIView.as_view(),name="product_business"),
    path("product/color/",Color_ProductListCreateAPIView.as_view(),name="product_color"),
    path("product/size/",Size_ProductListCreateAPIView.as_view(),name="product_size"),
    path("product/business/sell/",Business_ProductListCreateAPIView.as_view(),name="product_business"),
    path("size/",SizeListCreateAPIView.as_view(),name="size"),
    path("business/",BusinessListCreateAPIView.as_view(),name="business"),
    path("color/",ColorListCreateAPIView.as_view(),name="color"),
    path("collection/",CollectionListCreateAPIView.as_view(),name="collection"),
    path("indicator/",IndicatorListCreateAPIView.as_view(),name="indicator"),
    path("sex/",SexListCreateAPIView.as_view(),name="sex"),
    path("category/",CategoryListCreateAPIView.as_view(),name="category"),
    path("country/",CountryListCreateAPIView.as_view(),name="country"),
    path("reference/",ReferenceListCreateAPIView.as_view(),name="reference"),

    # Obtener un dato dado
    path("retrieve/product/<int:pk>/",ProductRetrieveAPIView.as_view(),name="product_pacht"),

    # Eliminar un dato segun lo dado
    path("destroy/product/<int:pk>/",ProductDestroyAPIView.as_view(),name="product_destroy"),

    # Actualizar un dato segun lo dado
    path("update/product/<int:pk>/",ProductUpdateAPIView.as_view(),name="product_update"),

    
]