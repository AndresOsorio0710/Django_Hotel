from django.contrib import admin


class PersonaAdmin(admin.ModelAdmin):
    search_fields = ['rut', 'apellido', 'nombre', 'correo', 'pais']
    list_display = ['rut', 'apellido', 'nombre', 'correo', 'pais']
    list_filter = ['pais']
    list_per_page = 10
