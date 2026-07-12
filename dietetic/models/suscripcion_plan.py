# dietetic/models/suscripcion_plan.py
from django.db import models
from .paciente import Paciente
from .plan_nutricional import PlanNutricional


class SuscripcionPlan(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('expirado', 'Expirado'),
        ('cancelado', 'Cancelado')
    ]

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='suscripciones'
    )
    plan = models.ForeignKey(
        PlanNutricional,
        on_delete=models.CASCADE,
        related_name='suscripciones'
    )
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='activo'
    )
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f'{self.paciente.full_name} - {self.plan.name} ({self.estado})'
