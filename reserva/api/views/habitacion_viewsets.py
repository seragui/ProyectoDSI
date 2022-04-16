from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from base.api import GeneralListApiView
from reserva.api.serializers.habitacion_serializers import *

class HabitacionViewSet(viewsets.ModelViewSet):
    serializer_class = HabitacionSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        habitacion_serializer=self.get_serializer(self.get_queryset(),many=True)
        return Response(habitacion_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Habitación creada correctamente!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            habitacion_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)

            if habitacion_serializer.is_valid():
                habitacion_serializer.save()
                return Response(habitacion_serializer.data, status=status.HTTP_200_OK)
            return Response(habitacion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        habitacion = self.get_queryset().filter(id=pk).first()
        if habitacion:
            habitacion.state = False
            habitacion.save()
            return Response({'message': 'Habitación Eliminada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe una habitación con esos datos'}, status=status.HTTP_400_BAD_REQUEST)
