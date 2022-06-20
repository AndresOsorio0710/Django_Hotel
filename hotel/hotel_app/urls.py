from django.urls import path
from hotel_app.views.administrador_app import administrador_inicio
from hotel_app.views.habitacion import habitacion_admin_inicio, habitacion_admin_agregar, habitacion_admin_eliminar, habitacion_admin_modificar
from hotel_app.views.hotel import hotel_admin_inicio, hotel_admin_agregar, hotel_admin_modificar, hotel_admin_eliminar
from hotel_app.views.hotel_app import hotel_inicio
from hotel_app.views.persona import persona_admin_inicio, persona_admin_agregar, persona_admin_eliminar, persona_admin_modificar
from hotel_app.views.registrar_usuario import registrar_usuario

urlpatterns = [
    path('', hotel_inicio, name='hotel_inicio'),
    path('resgistrar-usuario/', registrar_usuario, name="registrar_usuario"),
    # Administracion
    path('administrador/', administrador_inicio, name='administrador_inicio'),
    # Administrador - Habitacion
    path('administrador/hotel/<idh>/habitacion/',
         habitacion_admin_inicio, name="habitacion_admin_inicio"),
    path('administrador/hotel/<idh>/habitacion/agregar/',
         habitacion_admin_agregar, name="habitacion_admin_agregar"),
    path('administrador/hotel/<idh>/habitacion/eliminar/<id>/',
         habitacion_admin_eliminar, name="habitacion_admin_eliminar"),
    path('administrador/hotel/<idh>/habitacion/modificar/<id>/',
         habitacion_admin_modificar, name="habitacion_admin_modificar"),
    # Administrador - Hotel
    path('administrador/hotel/', hotel_admin_inicio,
         name="hotel_admin_inicio"),
    path('administrador/hotel/agregar/', hotel_admin_agregar,
         name="hotel_admin_agregar"),
    path('administrador/hotel/eliminar/<id>/', hotel_admin_eliminar,
         name="hotel_admin_eliminar"),
    path('administrador/hotel/modificar/<id>/', hotel_admin_modificar,
         name="hotel_admin_modificar"),
    # Administrador - Persona
    path('administrador/persona/', persona_admin_inicio,
         name="persona_admin_inicio"),
    path('administrador/persona/agregar/', persona_admin_agregar,
         name="persona_admin_agregar"),
    path('administrador/persona/eliminar/<id>/', persona_admin_eliminar,
         name="persona_admin_eliminar"),
    path('administrador/persona/modificar/<id>/', persona_admin_modificar,
         name="persona_admin_modificar"),
]
