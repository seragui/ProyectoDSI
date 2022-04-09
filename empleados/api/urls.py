from django.urls import path
from empleados.api.views.general_views import CargoAPIView, DepartamentoAPIView
from empleados.api.views.empleados_view import *

urlpatterns=[
    path('cargo/', CargoAPIView.as_view(),name='cargo_empleado'),
    path('departamento/', DepartamentoAPIView.as_view(),name='departamento_empleado'),
    path('empleado/',EmpleadosListCreateAPIView.as_view(),name='empleado'),
    path('gestionar/<int:pk>/',EmpleadosRetrieveUpdateDestroyAPIView.as_view(),name='empleado_gestionar')
]