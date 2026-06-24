from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Parroquia(models.Model):
    tipo_Parroquia = [
        ('URBANA', 'Urbana'),
        ('RURAL', 'Rural'),
    ]
    ubicacion_Parroquia = [
        ('NORTE', 'Norte'),
        ('SUR', 'Sur'),
        ('ESTE', 'Este'),
        ('OESTE', 'Oeste'),
    ]
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Parroquia")
    ubicacion = models.CharField(max_length=10, choices=ubicacion_Parroquia, verbose_name="Ubicación")
    tipo = models.CharField(max_length=10, choices=tipo_Parroquia, verbose_name="Tipo de Parroquia")

    def __str__(self):
        return self.nombre


class Barrio(models.Model):
    parques_rango = [(i, str(i)) for i in range(1, 7)]
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Barrio/Ciudadela")
    numero_viviendas = models.PositiveIntegerField(verbose_name="Número de Viviendas")
    numero_parques = models.IntegerField(choices=parques_rango, verbose_name="Número de Parques")
    numero_edificios_residenciales = models.PositiveIntegerField(verbose_name="Número de Edificios Residenciales")
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name='barrios', verbose_name="Parroquia")

    def __str__(self):
        return self.nombre


class PresidenteBarrio(models.Model):
    cedula = models.CharField(max_length=10, unique=True, verbose_name="Cédula de Identidad")
    nickname = models.CharField(max_length=50, unique=True, verbose_name="Nickname")
    edad = models.PositiveIntegerField(verbose_name="Edad")
    profesion = models.CharField(max_length=100, verbose_name="Profesión")
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, related_name='presidentes', verbose_name="Barrio")
    def __str__(self):
        return f"{self.nickname} ({self.profesion})"