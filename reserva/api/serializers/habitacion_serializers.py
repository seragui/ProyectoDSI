from reserva.models import Habitacion
from rest_framework import serializers

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        exclude=('state','created_date','modified_date','deleted_date')
        