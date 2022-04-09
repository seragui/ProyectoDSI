from rest_framework.routers import DefaultRouter
from empleados.api.views.empleados_viewsets import *

router = DefaultRouter()

router.register(r'empleados', EmpleadosViewSet, basename='empleados')

urlpatterns = router.urls
