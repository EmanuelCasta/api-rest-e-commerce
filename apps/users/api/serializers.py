from dataclasses import field, fields
from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):

    #Serializer user, these serializer send all attributtes
    class Meta:
        model = User
        fields = "__all__"