from django.db import models
from .paciente import Paciente


class LogroPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='logros')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, default='')
    fecha_logro = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_logro']

    def __str__(self):
        return f'{self.paciente.full_name} - {self.nombre} ({self.fecha_logro})'
