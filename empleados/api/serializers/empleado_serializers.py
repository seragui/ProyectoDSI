from empleados.models import Empleados
from rest_framework import serializers
from empleados.api.serializers.general_serializers import CargoSerializer, DepartamentoSerializer


class EmpleadosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empleados
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

"""
    def to_representation(self, instance):
        return{
            'id': instance.id,
            'nombres': instance.nombres,
            'apellidos': instance.apellidos,
            'fecha_nacimiento': instance.fecha_nacimiento,
            'nacionalidad': instance.nacionalidad,
            'dui': instance.dui,
            'isss': instance.isss,
            'nup': instance.nup,
            'direccion': instance.direccion,
            'ciudad': instance.ciudad,
            'telefono': instance.telefono,
            'sexo': instance.sexo,
            'fecha_contratacion': instance.fecha_contratacion,
            'id_cargo': instance.id_cargo.nombre_cargo,
            'id_departamento': instance.id_departamento.nombre_departamento
        }
"""
