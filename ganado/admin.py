# ganado/admin.py
from django.contrib import admin
from .models import Animal, Vacuna, Vacunacion

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('arete', 'nombre', 'raza', 'edad', 'estado_salud')
    list_filter = ('raza', 'sexo', 'estado_salud')
    search_fields = ('arete', 'nombre')
    
    def edad(self, obj):
        from datetime import date
        return date.today().year - obj.fecha_nacimiento.year

@admin.register(Vacunacion)
class VacunacionAdmin(admin.ModelAdmin):
    list_display = ('animal', 'vacuna', 'fecha_aplicacion', 'veterinario')
    list_filter = ('vacuna', 'fecha_aplicacion')
    date_hierarchy = 'fecha_aplicacion'