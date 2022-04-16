from rest_framework.routers import DefaultRouter
from reserva.api.views.habitacion_viewsets import *

router=DefaultRouter()

router.register(r'habitacion',HabitacionViewSet, basename='habitacion')
urlpatterns=router.urls