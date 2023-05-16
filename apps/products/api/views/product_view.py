from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework import generics

from apps.base.api import GeneralListApiView,GeneralListCreateApiView,GeneralRetrieveUpdateDestroyAPIView
from apps.products.api.serializers.product_serializers import *
from apps.products.models import Business_Product


# ===========================  Listar datos de los que se van a vender ["GET"] =======================
class Business_ProductShowListAPIView(GeneralListApiView):

    serializer_class = Business_Product_ShowSerializer

    def get(self,request):
        #Hacer una condicional que si esta logeado dar los 50 sino no dar los 5
        products_business = Business_Product.objects.all()[:20]
        users_serializer = self.serializer_class(products_business,many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

# =================================   Crear datos o listar ["GET", "POST"] =======================================
class ProductListCreateAPIView(GeneralListCreateApiView):
    serializer_class = ProductSerializer

    def post(self,request):
        serializers = self.serializer_class(data =request.data)

        if serializers.is_valid():
            serializers.save()
            return Response({"Messages":"Product create"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class Sex_BusinessListCreateAPIView(GeneralListCreateApiView):
    serializer_class = Sex_BusinessSerializer

class Color_ProductListCreateAPIView(GeneralListCreateApiView):
    serializer_class = Color_ProductSerializer

class Size_ProductListCreateAPIView(GeneralListCreateApiView):
    serializer_class = Size_ProductSerializer

class Business_ProductListCreateAPIView(GeneralListCreateApiView):
    serializer_class = Business_ProductSerializer

# ============================== Obtener una formacion con pk,Eliminar un dato ,Actualizar un dato ==============================
class ProductRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

class  Sex_BusinessRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = Sex_BusinessSerializer

class Color_ProductRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = Color_ProductSerializer

class Size_ProductRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = Size_ProductSerializer

class Business_ProductRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = Business_ProductSerializer





  



