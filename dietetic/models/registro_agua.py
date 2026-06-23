from django.db import models
from .paciente import Paciente


class RegistroAgua(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='registros_agua'
    )
    fecha = models.DateField()
    cantidad_ml = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f'{self.paciente.full_name} - {self.fecha} - {self.cantidad_ml}ml'
