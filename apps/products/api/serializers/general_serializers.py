from rest_framework import serializers
from apps.products.models import Business,Collection,Color,Indicator,Sex,Category,Size,Country,Reference


class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        exclude = ("state","modified_date","deleted_date","created_date")

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        exclude = ("state","modified_date","deleted_date","created_date")

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        exclude = ("state","modified_date","deleted_date","created_date")
    
class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicator
        exclude = ("state","modified_date","deleted_date","created_date")
    
class SexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sex
        exclude = ("state","modified_date","deleted_date","created_date")

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ("state","modified_date","deleted_date","created_date")

class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        exclude = ("state","modified_date","deleted_date","created_date")

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        exclude = ("state","modified_date","deleted_date","created_date")



class ReferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reference
        exclude = ("state","modified_date","deleted_date","created_date")
    