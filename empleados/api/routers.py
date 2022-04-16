from rest_framework.routers import DefaultRouter
from empleados.api.views.empleados_viewsets import *
from empleados.api.views.cargos_viewsets import *
from empleados.api.views.departamento_viewsets import *
router = DefaultRouter()

router.register(r'empleados', EmpleadosViewSet, basename='empleados')
router.register(r'cargo', CargoViewSet, basename='cargo')
router.register(r'departamento', DepartamentoViewSet, basename='departamento')
urlpatterns = router.urls
