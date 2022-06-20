from django import forms
from django.forms import ModelForm, Textarea, ValidationError
from hotel_app.models import Hotel


class HotelForm(ModelForm):

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        existe = Hotel.objects.filter(nombre__iexact=nombre).exists()
        if existe:
            raise ValidationError("Este nombre ya existe.")
        return nombre.upper()

    def clean_ciudad(self):
        ciudad = self.cleaned_data['ciudad']
        return ciudad.upper()

    def clean_direccion(self):
        direccion = self.cleaned_data['direccion']
        return direccion.upper()

    class Meta:
        model = Hotel
        fields = ["nombre", "ciudad", "direccion",
                  "logo", "imagen", "descripcion"]
        widgets = {
            'descripcion': Textarea(attrs={'cols': 40, 'rows': 6}),
        }
