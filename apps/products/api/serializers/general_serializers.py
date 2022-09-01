from apps.products.models import Business,Collection,Color,Indicator,Sex,Category,Size,Country,Reference
from rest_framework import serializers

class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        exclude = ("state,")

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        exclude = ("state,")

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        exclude = ("state,")
    
class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicator
        exclude = ("state,")
    
class SexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sex
        exclude = ("state,")

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ("state,")

class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        exclude = ("state,")

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        exclude = ("state,")



class ReferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reference
        exclude = ("state,")
    