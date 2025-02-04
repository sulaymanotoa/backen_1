from  django.shortcuts import render
from rest_framework import viewsets
from .models import Empleado
from .serializers import EmpleadoSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated #para que se accedan solo los usuarios con permisos esto se agg solo para explicar borrala depues si lo usamos
# Vista para el modelo Socios
class SociosViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [AllowAny] #todos pueden acceder a esta vista / API