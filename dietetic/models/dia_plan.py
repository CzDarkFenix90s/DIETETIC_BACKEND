from django.db import models
from .plan_nutricional import PlanNutricional


class DiaPlan(models.Model):
    plan_nutricional = models.ForeignKey(
        PlanNutricional,
        on_delete=models.CASCADE,
        related_name='dias_plan'
    )
    nombre_dia = models.CharField(max_length=100)
    orden = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['orden']
        unique_together = ['plan_nutricional', 'orden']

    def __str__(self):
        return f'{self.plan_nutricional.name} - {self.nombre_dia}'
