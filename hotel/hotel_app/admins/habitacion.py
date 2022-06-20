from django.contrib import admin


class HabitacionAdmin(admin.ModelAdmin):
    search_fields = ['hotel', 'numero', 'tipo', 'descripcion']
    list_display = ['numero', 'hotel',  'tipo', 'cama', 'valor']
    list_filter = ['hotel', 'tipo', 'cama']
    list_per_page = 10
