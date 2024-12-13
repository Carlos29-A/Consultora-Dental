from django.db import models

# Create your models here.
class Dentista(models.Model):
    nombre = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    contraseña = models.CharField(max_length=30, null=False, blank=False ,default="contraseña_defecto")

    def __str__(self):
        return self.nombre