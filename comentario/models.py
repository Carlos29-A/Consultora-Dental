from django.db import models
from django.contrib.auth.models import User
from citas.models import Citas
from dentista.models import Dentista
from django.utils.timezone import now
# Create your models here.
class Comentario(models.Model):
    contenido = models.CharField(max_length=100)
    calificacion = models.IntegerField()
    fecha_creacion = models.DateField(default=now)
    paciente_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cita_id = models.ForeignKey(Citas, on_delete=models.CASCADE)
    dentista_id = models.ForeignKey(Dentista, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name_plural = "comentarios"
        verbose_name ="comentario"
    def __str__(self):
        return self.contenido
    