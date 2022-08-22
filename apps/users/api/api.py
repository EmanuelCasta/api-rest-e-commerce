from xmlrpc.client import ResponseError
from rest_framework.views import APIView
from apps.users.api.serializers import UserSerializer
from apps.users.models import User
from rest_framework.response import Response

class UserAPIView(APIView):

    def get(self,request):
        users = User.objects.all()
        users_serializer = UserSerializer(users,many=True)
        return Response(users_serializer.data)

    def post(self,request):
        # json to model
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)