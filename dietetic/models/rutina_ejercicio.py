from django.db import models
from .plan_nutricional import PlanNutricional


class RutinaEjercicio(models.Model):
    plan_nutricional = models.ForeignKey(
        PlanNutricional,
        on_delete=models.CASCADE,
        related_name='rutinas_ejercicio'
    )
    descripcion_rutina = models.TextField()
    dias_semana = models.CharField(max_length=100)  # Ej: "Lunes, Miércoles, Viernes"
    duracion_minutos = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Rutina {self.plan_nutricional.name}'
