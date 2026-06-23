from django.db import models
from .paciente import Paciente


class HistorialClinico(models.Model):
    paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        related_name='historial_clinico'
    )
    alergias = models.TextField(blank=True, default='')
    enfermedades_cronicas = models.TextField(blank=True, default='')
    antecedentes_familiares = models.TextField(blank=True, default='')
    medicamentos_actuales = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Historial Clínico {self.paciente.full_name}'
