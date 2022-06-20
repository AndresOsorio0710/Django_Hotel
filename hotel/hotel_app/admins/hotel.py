from django.contrib import admin


class HotelAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'direccion', 'ciudad', ]
    list_display = ['nombre', 'direccion', 'ciudad', ]
    list_filter = ['ciudad']
    list_per_page = 10
