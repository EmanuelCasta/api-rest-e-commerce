from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from apps.base.api import GeneralDestroyAPIView, GeneralListApiView, GeneralRetrieveAPIView,GeneralUpdateAPIView,GeneralListCreateApiView
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

# ============================== Obtener una formacion con pk ==============================
class ProductRetrieveAPIView(GeneralRetrieveAPIView):
    serializer_class = ProductSerializer

# ================================ Eliminar un dato =======================================
class ProductDestroyAPIView(GeneralDestroyAPIView):
    serializer_class = ProductSerializer

# ================================ Actualizar un dato ========================================
class ProductUpdateAPIView(GeneralUpdateAPIView):
    serializer_class = ProductSerializer
 

