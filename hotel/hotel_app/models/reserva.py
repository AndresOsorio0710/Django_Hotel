from typing_extensions import Required
from django.db import models
from django.forms import ValidationError
from .persona import Persona


estados = [
    ("", "")
]


class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField('Código', max_length=16, blank=False, null=False)
    fecha_ingreso = models.DateField(
        'Fecha de ingreso', blank=False, null=False)
    fecha_salida = models.DateField('Fecha de salida', blank=False, null=False)
    estado = models.CharField(
        'Estado de la reserva', max_length=30, blank=False, null=False, choices=estados)
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
