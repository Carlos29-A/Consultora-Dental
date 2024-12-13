from django.db import models
from django.contrib.auth.models import User
from dentista.models import Dentista
# Create your models here.
class Citas(models.Model):
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Confirmada', 'Confirmada'),
        ('Cancelada', 'Cancelada')
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    motivo =models.CharField(max_length=100)
    id_usuario =models.ForeignKey(User,editable=False, on_delete=models.CASCADE, related_name='citas', verbose_name='Usuario')
    id_dentista =models.ForeignKey(Dentista,editable=False, on_delete=models.CASCADE, related_name='citas', verbose_name='Dentista' ,null=True)
    class Meta:
        verbose_name= 'Cita'
        verbose_name_plural ='Cita'

    def __str__(self):
        return f'{self.fecha_cita} + ": " {self.motivo}'