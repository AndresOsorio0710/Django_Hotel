from django.contrib import admin
from hotel_app.admins import HotelAdmin
from hotel_app.admins import HabitacionAdmin
from hotel_app.admins import PersonaAdmin
from hotel_app.models import Habitacion
from hotel_app.models import Hotel
from hotel_app.models import Persona


admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Persona, PersonaAdmin)
