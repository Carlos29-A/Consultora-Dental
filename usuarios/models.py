from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    correo =models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    rol = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    
class Mensaje(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    correo_electronico = models.EmailField(null=False, blank=False)
    asunto = models.CharField(max_length=255,null=False, blank=False)
    mensaje = models.TextField(null=False, blank=False)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.asunto}"