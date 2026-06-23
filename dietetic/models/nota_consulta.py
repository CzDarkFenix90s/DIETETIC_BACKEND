from django.db import models
from .consulta_dietetica import ConsultaDietetica


class NotaConsulta(models.Model):
    consulta = models.ForeignKey(
        ConsultaDietetica,
        on_delete=models.CASCADE,
        related_name='notas_consulta'
    )
    diagnostico = models.TextField(blank=True, default='')
    observaciones = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Nota {self.consulta}'
