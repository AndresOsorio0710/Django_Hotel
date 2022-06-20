from django.db import models


class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField('RUT o DNI de la persona', max_length=20, blank=False, null=False, unique=True)
    nombre = models.CharField('Nombre de la persona', max_length=50,blank=False, null=False,)
    apellido = models.CharField('Apellido(s) de la persona', max_length=50,blank=False, null=False,)
    pais = models.CharField('Pais de origen', max_length=20,blank=False, null=False)
    direccion = models.CharField('Dirección de origen', max_length=100, blank=False, null=False, )
    telefono = models.CharField('Número teléfonico d ela persona', max_length=10,blank=False, null=False)
    correo = models.EmailField('Correo electónico', blank=False, null=False, unique=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return self.apellido+' '+self.nombre