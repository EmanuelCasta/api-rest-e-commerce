from urllib import request
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

class BaseGeneralApi():
    serializer_class = None

    def get_queryset(self):
       model = self.get_serializer().Meta.model
       return model.objects.filter(state = True)

class GeneralListApiView(BaseGeneralApi,generics.ListAPIView):
    pass

class GeneralListCreateApiView(BaseGeneralApi,generics.ListCreateAPIView):
    pass

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

