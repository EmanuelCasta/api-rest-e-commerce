from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.models import User,Subscription,Membership

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id","username","email","name","last_name")

class UserSerializer(serializers.ModelSerializer):

    restrictions = ["<",">","/","`","!","[","]","*",":","^","+","\\","=","&"]
    #Serializer user, these serializer send all attributtes
    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):   

        for key, value in data.items():

            if  key != "last_login" and key != "password" and key != "groups" and key != "user_permissions":


                for restriction in self.restrictions:

                    if restriction in str(value) or str(value).startswith(" "):

                        raise serializers.ValidationError(f"Cannot contain special characters in the field {key}: {value}")
                    
        return data

    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        update_user =  super().update(instance, validated_data)
        update_user.set_password(validated_data["password"])
        update_user.save()
        return update_user

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

    def to_representation(self, instance):
        #Futura empresa
        return {
            "id": instance.id,
            "username" : instance.username,
            "email":instance.email,
            "name": instance.name,
            "last_name": instance.last_name,
            "image" : (instance.image if not hasattr(instance, 'image')  else None) ,
            "password": instance.password,
            "last_login":instance.last_login
        }

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        exclude = ("state","created_date", "modified_date","deleted_date")

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "count_sub": instance.count_sub,
            "count_sub_total": instance.count_sub_total,
            "proof_of_payment": instance.proof_of_payment,
            "expiration_date": instance.expiration_date,
            "membership": instance.membership.membership_type,
            "user": instance.user.email
        }

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        exclude = ("state","created_date", "modified_date","deleted_date")

"""
class TestUserSerializers(serializers.Serializer):

    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    # validar name
    def validate_name(self,value):
        if "develop" in value:
            raise serializers.ValidationError("Error no spuede existor usuario")
        return value

    # validar email
    def validate_email(self,value):

        if self.validate_name(self.context["name"]) in value:
            raise serializers.ValidationError("ok")

        return value

    def validate(self,data):
        if data["name"] in data["email"]:
            raise serializers.ValidationError("Email no puedo contener el nombre")
        return data

    # Meter al la base
    def  create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.save()
        return instance"""