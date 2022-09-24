from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from apps.users.api.serializers import CustomTokenObtainPairSerializer,CustomUserSerializer
from apps.users.models  import User



class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email","")
        password = request.data.get("password","")
        user = authenticate(
            email = email,
            password = password
        )
        if user:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    "token":login_serializer.validated_data.get("access"),
                    "refresh-token":login_serializer.validated_data.get("refresh"),
                    "user":user_serializer.data,
                    "message":"Bienvenido has iniciado sesion correctame"

                },status= status.HTTP_200_OK)
        return Response({"Error":"Contraseña o nombre de usuarios incorrectos"},status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    def post(self,request,*agrs,**kwargs):
        user = User.objects.filter(id=request.data.get("user",""))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({"Message":" Se cerro la sesion correctamente"})
        return Response({"Message":" No usuario iniciado"})