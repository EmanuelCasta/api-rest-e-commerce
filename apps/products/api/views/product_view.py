from rest_framework import status
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.products.api.serializers.product_serializers import *
from apps.products.models import Business_Product



class ProductListAPIView(GeneralListApiView):
    serializer_class = ProductSerializer

class Sex_BusinessListAPIView(GeneralListApiView):
    serializer_class = Sex_BusinessSerializer

class Color_ProductAPIView(GeneralListApiView):
    serializer_class = Color_ProductSerializer

class Size_ProductListAPIView(GeneralListApiView):
    serializer_class = Size_ProductSerializer

class Business_ProductListAPIView(GeneralListApiView):
    serializer_class = Business_ProductSerializer

class Business_ProductShowListAPIView(GeneralListApiView):
    serializer_class = Business_Product_ShowSerializer

    def get(self,request):
        #Hacer una condicional que si esta logeado dar los 50 sino no dar los 5
        products_business = Business_Product.objects.all()[:20]
        users_serializer = self.serializer_class(products_business,many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)