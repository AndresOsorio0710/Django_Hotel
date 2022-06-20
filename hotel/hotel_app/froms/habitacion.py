from django.forms import ModelForm, Textarea, NumberInput
from hotel_app.models import Habitacion


class HabitacionForm(ModelForm):

    def clean_hospedaje(self):
        hospedaje = self.cleaned_data['hospedaje']
        return hospedaje.upper()

    class Meta:
        model = Habitacion
        fields = ['numero', 'tipo', 'cama', 'hospedaje',
                  'valor', 'imagen', 'descripcion']
    widgets = {
        'descripcion': Textarea(attrs={'cols': 40, 'rows': 6}),
        'numero': NumberInput(attrs={'min': 0}),
    }
