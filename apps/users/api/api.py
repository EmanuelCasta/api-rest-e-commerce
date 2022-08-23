from rest_framework import status
from rest_framework.views import APIView
from apps.users.api.serializers import UserSerializer
from apps.users.models import User
from rest_framework.response import Response

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
        users_serializer = UserSerializer(users,many=True)
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
        if user:
            user_serializer = UserSerializer(user,data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data,status=status.HTTP_302_FOUND)
            return Response(user_serializer.errors,status=status.HTTP_304_NOT_MODIFIED)
        return Response(self.messages,status=status.HTTP_304_NOT_MODIFIED)
