from django.db import models
from .paciente import Paciente


class ProgresoFoto(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='progresos_fotos'
    )
    foto = models.ImageField(upload_to='progresos_fotos/')
    descripcion = models.TextField(blank=True, default='')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_subida']
        verbose_name_plural = 'Progresos Fotos'

    def __str__(self):
        return f'Foto {self.paciente.full_name} - {self.fecha_subida.date()}'
