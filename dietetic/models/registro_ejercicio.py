from django.db import models
from .paciente import Paciente
from .rutina_ejercicio import RutinaEjercicio


class RegistroEjercicio(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='registros_ejercicio')
    rutina_ejercicio = models.ForeignKey(RutinaEjercicio, on_delete=models.CASCADE, related_name='registros')
    fecha = models.DateField()
    completado = models.BooleanField(default=False)
    notas = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha']
        unique_together = ['paciente', 'rutina_ejercicio', 'fecha']

    def __str__(self):
        return f'{self.paciente.full_name} - {self.rutina_ejercicio.descripcion_rutina} - {self.fecha}'
