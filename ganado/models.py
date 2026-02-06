# ganado/models.py
from django.db import models

class Animal(models.Model):
    arete = models.CharField(max_length=50, unique=True)  # Identificación
    nombre = models.CharField(max_length=100, blank=True)
    raza = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Macho'), ('H', 'Hembra')])
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    estado_salud = models.CharField(max_length=20, choices=[
        ('SANO', 'Sano'),
        ('ENFERMO', 'Enfermo'),
        ('TRATAMIENTO', 'En tratamiento')
    ])
    foto = models.ImageField(upload_to='animales/', blank=True)
    
    def __str__(self):
        return f"{self.arete} - {self.nombre}"

class Vacuna(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    lote = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    
    def __str__(self):
        return self.nombre

class Vacunacion(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    fecha_aplicacion = models.DateField()
    dosis = models.CharField(max_length=50)
    veterinario = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Vacunaciones"