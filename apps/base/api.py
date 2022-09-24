
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone

from apps.users.models import Subscription,Membership,User
from apps.users.api.serializers import SubscriptionSerializer


class BaseGeneralApi():
    serializer_class = None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state = True)

class GeneralListApiView(BaseGeneralApi,generics.ListAPIView):
    
    def list(self,request):
        # Comprobar los si esta inicionado sesion sino dar los 50
        table_serializer = self.get_serializer(self.get_queryset()[:3],many=True)
        return Response(table_serializer.data , status= status.HTTP_200_OK)

class GeneralRetrieveAPIView(BaseGeneralApi,generics.RetrieveAPIView):
    pass

class GeneralUpdateAPIView(BaseGeneralApi,generics.UpdateAPIView):
    
    def get_queryset(self,pk):
       model = self.get_serializer().Meta.model
       return model.objects.filter(state = True).filter(id=pk).first()

    def patch(self, request, pk=None):
        table = self.get_queryset(pk)

        if table:
            table_serializer = self.serializer_class(table)
            return Response(table_serializer.data,status=status.HTTP_200_OK)
        return Response({"message":f"No se pudo encontrar la caracteristica {pk}"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,resquest,pk=None):
        table = self.get_queryset(pk)

        if table:
            table_serializer = self.serializer_class(table,data = resquest.data)
            if table_serializer.is_valid():
                table_serializer.save()
                return Response(table_serializer.data, status=status.HTTP_200_OK)
            return Response(table_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class GeneralDestroyAPIView(BaseGeneralApi,generics.DestroyAPIView):
    
    
    def delete(self, request, pk=None):
        table = self.get_queryset().filter(id=pk).first()

        if table:
            table.state = False
            table.save()
            return Response({"message":"Se elimino correctamente"},status=status.HTTP_200_OK)
        return Response({"message":"No se pudo encontrar"},status=status.HTTP_400_BAD_REQUEST)

# Complete viewset

class GeneralViewSetAPIView(viewsets.ModelViewSet):
    serializer_class = None
    permission_classes = (IsAuthenticated,)
    number_data_free = 13

    def get_queryset(self,user=None,pk=None):
        if user is not None:
            return self.get_serializer().Meta.model.objects.filter(state =True).filter(user = user).first()
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state =True)
        model = self.get_serializer().Meta.model
        return model.objects.filter(state = True).filter(id=pk).first()

    def check_subs_databases(self,timeExpiration,type,request):
        if type != "Free":
            if timeExpiration>= timezone.now():  
                return True
            else:
                print("=======================2")
                user_membership = Subscription.objects.filter(state = True).filter(user = request.user).first()
                user_membership.membership=Membership.objects.get(slug="Free")
                user_membership.save()
                return False

        return False


    def list(self,request):
        user_membership = Subscription.objects.filter(user = request.user).first()
        check = self.check_subs_databases(user_membership.expiration_date,user_membership.membership.membership_type,request)
      
        if check:
            #Tiene sub
            table_serializer = self.get_serializer(self.get_queryset(),many=True)
            return Response(table_serializer.data, status= status.HTTP_200_OK)

       
        table_serializer = self.get_serializer(self.get_queryset()[:self.number_data_free],many=True)
        return Response({"data":table_serializer.data,"Message":"La subscripcion vencio el dia "+str(user_membership.expiration_date)} , status= status.HTTP_200_OK)
        
        

    def destroy(self, request, pk=None):
        table = self.get_queryset(pk)

        if table:
            table.state = False
            table.save()
            return Response({"message":"Se elimino correctamente"},status=status.HTTP_200_OK)
        return Response({"message":"No se pudo encontrar"},status=status.HTTP_400_BAD_REQUEST)

    def update(self,resquest,pk=None):
        table = self.get_queryset(pk)

        if table:
            table_serializer = self.serializer_class(table,data = resquest.data)
            if table_serializer.is_valid():
                table_serializer.save()
                return Response(table_serializer.data, status=status.HTTP_200_OK)
            return Response(table_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class GeneralViewSetAPIViewLIMIT(GeneralViewSetAPIView):

    def list(self,request):
        sub = self.get_queryset(user = request.user)
        serializer_sub = self.get_serializer(sub)
        return Response(serializer_sub.data , status= status.HTTP_200_OK)

# Complete 
class GeneralListCreateApiView(BaseGeneralApi,generics.ListCreateAPIView):
    pass

class GeneralRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state =True)
        model = self.get_serializer().Meta.model
        return model.objects.filter(state = True).filter(id=pk).first()
    

    def patch(self, request, pk=None):
        table = self.get_queryset(pk)

        if table:
            table_serializer = self.serializer_class(table)
            return Response(table_serializer.data,status=status.HTTP_200_OK)
        return Response({"message":f"No se pudo encontrar la caracteristica {pk}"},status=status.HTTP_400_BAD_REQUEST)

    def put(self,resquest,pk=None):
        table = self.get_queryset(pk)

        if table:
            table_serializer = self.serializer_class(table,data = resquest.data)
            if table_serializer.is_valid():
                table_serializer.save()
                return Response(table_serializer.data, status=status.HTTP_200_OK)
            return Response(table_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        table = self.get_queryset(pk)

        if table:
            table.state = False
            table.save()
            return Response({"message":"Se elimino correctamente"},status=status.HTTP_200_OK)
        return Response({"message":"No se pudo encontrar"},status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        table = self.get_queryset(pk)

        if table:
            table_serializer = self.serializer_class(table)
            return Response(table_serializer.data,status=status.HTTP_200_OK)
        return Response({"message":f"No se pudo encontrar la caracteristica {pk}"},status=status.HTTP_400_BAD_REQUEST)