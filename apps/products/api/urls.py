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

    # Obtener un dato dado, Eliminar un dato segun lo dado, actualizar
    path("product/<int:pk>/",ProductRetrieveUpdateDestroyAPIView.as_view(),name="product_pacht"),
    path("product/sex/<int:pk>/",Sex_BusinessRetrieveUpdateDestroyAPIView.as_view(),name="product_pacht"),
    path("product/color/<int:pk>/",Color_ProductRetrieveUpdateDestroyAPIView.as_view(),name="product_color"),
    path("product/size/<int:pk>/",Size_ProductRetrieveUpdateDestroyAPIView.as_view(),name="product_sizes"),
    path("product/business/sell/<int:pk>/",Business_ProductRetrieveUpdateDestroyAPIView.as_view(),name="product_business"),
    path("size/<int:pk>/",SizeRetrieveUpdateDestroyAPIView.as_view(),name="size"),
    path("business/<int:pk>/",BusinessRetrieveUpdateDestroyAPIView.as_view(),name="business"),
    path("color/<int:pk>/",ColorRetrieveUpdateDestroyAPIView.as_view(),name="color"),
    path("collection/<int:pk>/",CollectionRetrieveUpdateDestroyAPIView.as_view(),name="collection"),
    path("indicator/<int:pk>/",IndicatorRetrieveUpdateDestroyAPIView.as_view(),name="indicator"),
    path("sex/<int:pk>/",SexRetrieveUpdateDestroyAPIView.as_view(),name="sex"),
    path("category/<int:pk>/",CategoryRetrieveUpdateDestroyAPIView.as_view(),name="category"),
    path("country/<int:pk>/",CountryRetrieveUpdateDestroyAPIView.as_view(),name="country"),
    path("reference/<int:pk>/",ReferenceRetrieveUpdateDestroyAPIView.as_view(),name="reference"),
    

    
    

    
]