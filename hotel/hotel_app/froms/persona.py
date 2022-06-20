from django.forms import ModelForm, TextInput
from hotel_app.models import Persona


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ["rut", "nombre", "apellido",
                  "pais", "direccion", "telefono", "correo"]
