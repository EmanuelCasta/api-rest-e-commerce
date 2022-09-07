from rest_framework import generics
from apps.products.api.serializers.general_serializers import BusinessSerializer,CollectionSerializer,ColorSerializer,CategorySerializer,CountrySerializer,IndicatorSerializer,ReferenceSerializer,SexSerializer,SizeSerializer
from apps.base.api import GeneralListApiView

class BusinessListAPIView(GeneralListApiView):
    
    serializer_class = BusinessSerializer

    
class ColorListAPIView(GeneralListApiView):
    
    serializer_class = ColorSerializer


class CollectionListAPIView(GeneralListApiView):
    
    serializer_class = CollectionSerializer


class IndicatorListAPIView(GeneralListApiView):
    
    serializer_class = IndicatorSerializer


class SexListAPIView(GeneralListApiView):
    
    serializer_class = SexSerializer

class CategoryListAPIView(GeneralListApiView):
    
    serializer_class = CategorySerializer


class CountryListAPIView(GeneralListApiView):
    
    serializer_class = CountrySerializer

    

class SizeListAPIView(GeneralListApiView):
    
    serializer_class = SizeSerializer



class ReferenceListAPIView(GeneralListApiView):
    
    serializer_class = ReferenceSerializer

