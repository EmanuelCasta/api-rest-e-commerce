from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import  viewsets

from apps.users.api.serializers import UserSerializer,UserListSerializer,MembershipSerializer,SubscriptionSerializer
from apps.base.api import GeneralListApiView,GeneralViewSetAPIViewLIMIT


class MemberListAPIVIEW(GeneralListApiView):
    serializer_class = MembershipSerializer


class SubcriptionsViewSet(GeneralViewSetAPIViewLIMIT):
    serializer_class = SubscriptionSerializer


class UserViewSet(viewsets.GenericViewSet):
    serializer_class =UserSerializer
    list_serializer_class = UserListSerializer 
    #serializer_class_sub = SubscriptionSerializer

    def get_object(self,pk):
        return get_object_or_404(self.serializer_class.Meta.model,pk=pk)

    def get_queryset(self):
        if self.queryset is  None:
            self.queryset = self.serializer_class().Meta.model.objects.filter(is_active=True)
        return self.queryset

    def list(self,request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users,many=True)
        return Response(users_serializer.data,status=status.HTTP_200_OK)

    def create(self,request):
        user = self.serializer_class(data=request.data)
        if user.is_valid():
            user.save()
            #self.serializer_class_sub().Meta.model.objects.cre
            return Response({"message":"Usuario registrado"},status=status.HTTP_200_OK)
        return Response({"message":"Error de usuario registrado","error":user.errors},status=status.HTTP_200_OK)

    def retrieve(self,request,pk=None):
        user= self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)

    def update(self,request,pk=None):
        user = self.get_object(pk)
        if user:
            user_serializer = self.serializer_class(user,data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data,status=status.HTTP_302_FOUND)
            return Response(user_serializer.errors,status=status.HTTP_304_NOT_MODIFIED)
        return Response({"message":"Not found user"},status=status.HTTP_304_NOT_MODIFIED)
    
    def destroy(self,request,pk=None):
        user_destroy = self.serializer_class().Meta.model.objects.filter(id=pk).update(is_active=True)
        if user_destroy == 1:
            return Response({"message":"Usuario eliminado correctamente"})
        return Response({"message":"Usuario no existe"})
    


"""
class UserAPIView(APIView):

    # error messages
    messages = {"message":"Not found user"}

    # Method to find 1 or all users with or without pk
    def get(self,request, pk=None):

        # Find 1 user witk ok
        if pk is not None:
            user = User.objects.filter(id=pk).first()
            if user:
                users_serializer = UserSerializer(user)
                return Response(users_serializer.data, status=status.HTTP_200_OK)
            return Response(self.messages, status=status.HTTP_404_NOT_FOUND)

        # Find all users without pk
        users = User.objects.all()
        users_serializer = UserListSerializer(users,many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    # Method to create user
    def post(self,request):

        # convert json to model and validated
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    

    # Delete user
    def delete(self,request,pk):
        user = User.objects.filter(id=pk).first()
        if user:
            user.delete()
            return Response({"status":status.HTTP_200_OK},status=status.HTTP_200_OK)
        return Response(self.messages,status=status.HTTP_304_NOT_MODIFIED)

    # Update user 
    def put(self,request,pk):
        user = User.objects.filter(id=pk).first()
        print(pk,"===============================================")
        if user:
            user_serializer = UserSerializer(user,data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data,status=status.HTTP_302_FOUND)
            return Response(user_serializer.errors,status=status.HTTP_304_NOT_MODIFIED)
        return Response(self.messages,status=status.HTTP_304_NOT_MODIFIED)
"""