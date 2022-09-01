from apps.products.models import Product,Sex_Business,Color_Product,Size_Product,Business_Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ("state,")

class Sex_BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sex_Business
        exclude = ("state,")

class Color_ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color_Product
        exclude = ("state,")

class Size_ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size_Product
        exclude = ("state,")

class Business_ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business_Product
        exclude = ("state,")