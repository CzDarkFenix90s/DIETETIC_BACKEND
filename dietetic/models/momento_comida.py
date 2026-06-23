from django.db import models
from .dia_plan import DiaPlan


class MomentoComida(models.Model):
    dia_plan = models.ForeignKey(
        DiaPlan,
        on_delete=models.CASCADE,
        related_name='momentos_comida'
    )
    nombre_momento = models.CharField(max_length=100)
    orden = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['orden']
        unique_together = ['dia_plan', 'orden']

    def __str__(self):
        return f'{self.dia_plan.nombre_dia} - {self.nombre_momento}'
