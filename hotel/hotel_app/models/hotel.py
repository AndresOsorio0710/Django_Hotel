from django.db import models


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del hotel', max_length=40,
                              blank=False, null=False,)
    descripcion = models.TextField(
        'Descripción del hotel', blank=False, null=False, )
    logo = models.ImageField(
        'Logo del hotel', upload_to='hotel/logo/%Y/%m/%d', null=True, blank=True)
    imagen = models.ImageField(
        'Imagen del hotel', upload_to='hotel/imagen/%Y/%m/%d', null=True, blank=True)
    direccion = models.CharField('Dirección del hotel', max_length=100,
                                 blank=False, null=False, )
    ciudad = models.CharField('Ciudad del hotel', max_length=50,
                              blank=False, null=False, )

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hoteles'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
