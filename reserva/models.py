from django.db import models
from base.models import BaseModel
# Create your models here.

class Habitacion(BaseModel):
    tipo_habitacion=models.CharField("Tipo de Habitación", max_length=100,blank=False, null=False)
    caracteristicas=models.TextField('Características',max_length=500,blank=False, null=False)
    numero_habitacion=models.IntegerField('Número de Habitación',blank=False, null=False)
    precio=models.DecimalField('Precio',max_digits=6, decimal_places=2, blank=False,null=False)
    numero_piso=models.IntegerField('Número de Piso',blank=False,null=False)
    estado_habitacion=models.BooleanField('Estado Habitación',blank=False, null=False,default=False)

    class Meta:
        verbose_name=('Habitacion')
        verbose_name_plural=('Habitaciones')

    def __str__(self):
        return self.tipo_habitacion
     