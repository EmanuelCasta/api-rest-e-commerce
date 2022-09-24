from rest_framework import generics

from apps.products.api.serializers.general_serializers import (
    BusinessSerializer,CollectionSerializer,ColorSerializer,CategorySerializer,CountrySerializer,IndicatorSerializer,ReferenceSerializer,SexSerializer,SizeSerializer)
from apps.base.api import GeneralListCreateApiView,GeneralRetrieveUpdateDestroyAPIView



# =====================  Crear Productos o listar ["GET", "POST"]==========================
class BusinessListCreateAPIView(GeneralListCreateApiView): 
    serializer_class = BusinessSerializer

class ColorListCreateAPIView(GeneralListCreateApiView): 
    serializer_class = ColorSerializer

class CollectionListCreateAPIView(GeneralListCreateApiView): 
    serializer_class = CollectionSerializer

class IndicatorListCreateAPIView(GeneralListCreateApiView):  
    serializer_class = IndicatorSerializer

class SexListCreateAPIView(GeneralListCreateApiView):  
    serializer_class = SexSerializer

class CategoryListCreateAPIView(GeneralListCreateApiView):
    serializer_class = CategorySerializer

class CountryListCreateAPIView(GeneralListCreateApiView):
    serializer_class = CountrySerializer
  
class SizeListCreateAPIView(GeneralListCreateApiView):
    serializer_class = SizeSerializer

class ReferenceListCreateAPIView(GeneralListCreateApiView):
    serializer_class = ReferenceSerializer

# ============================== UPDATE, DELETE, PATCH, PUT ====================
class BusinessRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = BusinessSerializer

class ColorRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView): 
    serializer_class = ColorSerializer

class CollectionRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView): 
    serializer_class = CollectionSerializer

class IndicatorRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):  
    serializer_class = IndicatorSerializer

class SexRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):  
    serializer_class = SexSerializer

class CategoryRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

class CountryRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = CountrySerializer
  
class SizeRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = SizeSerializer

class ReferenceRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = ReferenceSerializer