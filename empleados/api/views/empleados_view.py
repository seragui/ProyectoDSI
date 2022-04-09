from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from base.api import GeneralListApiView
from empleados.api.serializers.empleado_serializers import EmpleadosSerializer


class EmpleadosListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = EmpleadosSerializer
    queryset=EmpleadosSerializer.Meta.model.objects.filter(state=True)

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Empleado creado correctamente!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpleadosRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmpleadosSerializer

    def get_queryset(self,pk=None):
        return self.get_serializer().Meta.model.objects.filter(id=pk,state=True).first()
    
    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            empleado_serializer=self.serializer_class(self.get_queryset(pk))
            return Response(empleado_serializer.data, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un empleado con esos datos'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            empleado_serializer=self.serializer_class(self.get_queryset(pk),data=request.data)

            if empleado_serializer.is_valid():
                empleado_serializer.save()
                return Response(empleado_serializer.data,status=status.HTTP_200_OK)
            return Response(empleado_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        empleado = self.get_queryset().filter(id=pk).first()
        if empleado:
            empleado.state = False
            empleado.save()
            return Response({'message': 'Empleado Eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un empleado con esos datos'}, status=status.HTTP_400_BAD_REQUEST)



    


    
