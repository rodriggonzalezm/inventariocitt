from django.contrib import admin
from .models import Cliente, Cortinas
# Register your models here.

class CortinasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ancho', 'alto', 'direccion', 'numerotelefono']
    search_fields = ['nombre']
    list_filter = ['nombre']
    list_per_page = 10

admin.site.register(Cliente)
admin.site.register(Cortinas, CortinasAdmin)