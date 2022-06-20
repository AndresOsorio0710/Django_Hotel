from django.db import models
from django.forms import ValidationError
from .hotel import Hotel


tipos = [
    ("HABITACIÓN ESTÁNDAR", "HABITACIÓN ESTÁNDAR"),
    ("HABITACIÓN PRESIDENCIAL", "HABITACIÓN PRESIDENCIAL"),
    ("HABITACIÓN SUITE ROYAL", "HABITACIÓN SUITE ROYAL"),
    ("HABITACIÓN FAMILIAR", "HABITACIÓN FAMILIAR"),
    ("HABITACIÓN KING", "HABITACIÓN KING"),
    ("HABITACIÓN QUEEN", "HABITACIÓN QUEEN")
]


camas = [
    ("DOBLE", "DOBLE"),
    ("MATRIMONIAL", "MATRIMONIAL"),
    ("SENCILLA", "SENCILLA")
]


def solo_numeros(value):
    if value.isdigit() == False:
        raise ValidationError('Este campo solo permite números.')


def validar_valor(valor):
    if valor < 0:
        raise ValidationError('El valor mínimo permitido es $0.')


class Habitacion(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.CharField('Número de habitación',max_length=4, blank=False, null=False, validators=[solo_numeros])
    tipo = models.CharField('Tipo de habitación', max_length=30, blank=False, null=False, choices=tipos)
    cama = models.CharField('Tipo de cama', max_length=30,blank=False, null=False, choices=camas)
    hospedaje = models.CharField('Identificador de hospedaje', max_length=50, blank=False, null=False)
    valor = models.IntegerField('Valor de la habitación', validators=[validar_valor])
    imagen = models.ImageField('Imagen de la habitación', upload_to='habitacion/imagen/%Y/%m/%d', null=True, blank=True)
    descripcion = models.TextField('Descripción de la habitación', blank=False, null=False, )
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT)
   
    class Meta:
        verbose_name = 'Habitación'
        verbose_name_plural = 'Habitaciones'
        ordering = ['hotel','numero']


    def __str__(self):
        return self.numero