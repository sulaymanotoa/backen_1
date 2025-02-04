from django.db import models
from .choise import CARGO
from django.core.validators import MinValueValidator,MaxValueValidator,MaxLengthValidator,MinLengthValidator
from.Validadores import validacion_numeros

class Empleado(models.Model):
   cedula = models.CharField(max_length=10, primary_key=True validators=[MinLengthValidator(10)])
   nombre = models.CharField(max_length=50)
   apellido = models.CharField(max_length=50), verbose_name = 'apellido',
   direccion = models.CharField(max_length=100)
   telefono = models.CharField(max_length=15)
   email = models.EmailField()
   cargo = models.CharField(max_length=50, choise=CARGO)
   
class Meta:
 verbose_name = 'Empleado'
 verbose_name_plural = 'Empleados'
 db_table = 'Empleado'
 def __str__(self):
   return self.nombre
    
     



