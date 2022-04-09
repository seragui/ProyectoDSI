from base.api import GeneralListApiView

from empleados.models import Cargo, Departamento
from empleados.api.serializers.general_serializers import CargoSerializer, DepartamentoSerializer

class CargoAPIView(GeneralListApiView):
    serializer_class= CargoSerializer

class DepartamentoAPIView(GeneralListApiView):
    serializer_class= DepartamentoSerializer

