from django.db import models
from .momento_comida import MomentoComida
from .alimento_programado import AlimentoProgramado


class DetallePlanAlimento(models.Model):
    momento_comida = models.ForeignKey(
        MomentoComida,
        on_delete=models.CASCADE,
        related_name='detalles_alimentos'
    )
    alimento_programado = models.ForeignKey(
        AlimentoProgramado,
        on_delete=models.CASCADE,
        related_name='detalles_plan'
    )
    cantidad_gramos = models.DecimalField(max_digits=7, decimal_places=2)
    orden = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['orden']
        unique_together = ['momento_comida', 'alimento_programado']

    def __str__(self):
        return f'{self.momento_comida} - {self.alimento_programado.name}'
