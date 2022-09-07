from rest_framework import serializers

from apps.products.models import Product,Sex_Business,Color_Product,Size_Product,Business_Product
from apps.products.api.serializers.general_serializers import  SexSerializer



class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    collection = serializers.StringRelatedField()
    business = serializers.StringRelatedField()
    reference = serializers.StringRelatedField()
    
    class Meta:
        model = Product
        exclude = ("state","modified_date","deleted_date","created_date")


class Business_ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business_Product
        exclude = ("state","modified_date","deleted_date","created_date")

    def to_representation(self, instance):
        return {
            # Se llama la variable de ese modelo y luego se llama la variable del otro modelo
             "id": 1,
            "price": instance.price,
            "discount": instance.discount/100,
            "date": instance.date,
            "qualification": instance.qualification,
            "count_qualification": instance.count_qualification,
            "product": instance.product.name,
            "business": instance.business.name,
            "country": instance.country.name
        }

class Business_Product_ShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business_Product
        exclude = ("state","modified_date","deleted_date","created_date")

    def to_representation(self, instance):
        return {
            # Se llama la variable de ese modelo y luego se llama la variable del otro modelo
             "id": 1,
            "price": instance.price,
            "discount": instance.discount/100,
            "date": instance.date,
            "qualification": instance.qualification,
            "count_qualification": instance.count_qualification,
            "product": instance.product.name,
            "business_sells": instance.business.name,
            "business_product": instance.product.business.name,
            "country": instance.country.name,
            "category": instance.product.category.name,
            "collection": instance.product.collection.name,
            
        }
        
class Sex_BusinessSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Sex_Business
        exclude = ("state","modified_date","deleted_date","created_date")

    def to_representation(self, instance):
        return {
            # Se llama la variable de ese modelo y luego se llama la variable del otro modelo
            "sex" : instance.sex.name,
            "business" : instance.businnes_producto.business.name
        }
    
    

class Color_ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color_Product
        exclude = ("state","modified_date","deleted_date","created_date")

class Size_ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size_Product
        exclude = ("state","modified_date","deleted_date","created_date")

