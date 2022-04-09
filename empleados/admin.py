from django.contrib import admin
from empleados.models import *
# Register your models here.

class CargoAdmin(admin.ModelAdmin):
    list_display=('id','nombre_cargo')

class DepartamentoAdmin(admin.ModelAdmin):
    list_display=('id','nombre_departamento')

admin.site.register(Empleados)
admin.site.register(Cargo,CargoAdmin)
admin.site.register(Departamento,DepartamentoAdmin)
