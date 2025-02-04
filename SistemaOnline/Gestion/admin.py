from django.contrib import admin

from.models import(Empleado)

admin.site.register(Empleado)
class EmpleadoAdmin(admin..ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'direccion', 'telefono', 'email', 'cargo') 
    search_fields = ('cedula','nombre', 'apellido')
    list_filter = ('cedula','apellido')




