from django.core.exceptions import ValidationError

def validacion_numeros(value):
    if not value.isdigit():
        raise ValueError("El valor debe contener solo numeros")
