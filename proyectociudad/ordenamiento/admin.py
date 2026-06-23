from django.contrib import admin
from ordenamiento.models import Parroquia, Barrio, PresidenteBarrio
# Register your models here.

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    list_filter = ('ubicacion', 'tipo')
    search_fields = ('nombre',)

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales', 'parroquia')
    list_filter = ('parroquia',)
    search_fields = ('nombre',)

class PresidenteBarrioAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nickname', 'edad', 'profesion', 'barrio')
    list_filter = ('profesion',)
    search_fields = ('nickname', 'cedula')

admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Barrio, BarrioAdmin)
admin.site.register(PresidenteBarrio, PresidenteBarrioAdmin)