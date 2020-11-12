from django.contrib import admin
from .models import Cliente, Cortinas
# Register your models here.

class CortinasAdmin(admin.ModelAdmin):
    list_display = ['rut', 'alto', 'ancho']
    search_fields = ['rut']
    list_filter = ['alto']
    list_per_page = 10

admin.site.register(Cliente)
admin.site.register(Cortinas, CortinasAdmin)