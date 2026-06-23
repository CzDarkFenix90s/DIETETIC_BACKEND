from django.db import models
from .paciente import Paciente
from .momento_comida import MomentoComida


class SeguimientoConsumo(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='seguimientos_consumo'
    )
    momento_comida = models.ForeignKey(
        MomentoComida,
        on_delete=models.CASCADE,
        related_name='seguimientos_consumo'
    )
    fecha = models.DateField()
    completado = models.BooleanField(default=False)
    notas = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']
        unique_together = ['paciente', 'momento_comida', 'fecha']

    def __str__(self):
        return f'{self.paciente.full_name} - {self.fecha} - {self.momento_comida.nombre_momento}'
