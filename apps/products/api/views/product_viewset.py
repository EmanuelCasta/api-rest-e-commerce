from apps.base.api import GeneralViewSetAPIView,GeneralListApiView
from apps.products.api.serializers.product_serializers import *



class ProductViewSetAPIView(GeneralViewSetAPIView):
    serializer_class = ProductSerializer

class  Sex_BusinessViewSetAPI(GeneralViewSetAPIView):
    serializer_class = Sex_BusinessSerializer

class Color_ProductViewSetAPI(GeneralViewSetAPIView):
    serializer_class = Color_ProductSerializer

class Size_ProductViewSetAPI(GeneralViewSetAPIView):
    serializer_class = Size_ProductSerializer

class Business_ProductViewSetAPI(GeneralViewSetAPIView):
    serializer_class = Business_ProductSerializer

class Business_ProductShowViewSetAPI(GeneralListApiView):
    serializer_class = Business_Product_ShowSerializer

    