# dietetic/models/alimento_programado.py
from django.db import models
from .plan_nutricional import PlanNutricional
from .categoria_alimento import CategoriaAlimento


class AlimentoProgramado(models.Model):
    MEAL_CHOICES = [
        ('desayuno', 'Desayuno'),
        ('almuerzo', 'Almuerzo'),
        ('cena', 'Cena'),
        ('snack', 'Snack'),
    ]

    name               = models.CharField(max_length=200)
    description        = models.TextField(blank=True, default='')
    portion_grams      = models.DecimalField(max_digits=10, decimal_places=2, default=100.0)

    # Nuevos campos para Macros (Maestro)
    calories           = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    protein            = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    carbs              = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    fat                = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    meal_type          = models.CharField(max_length=20, choices=MEAL_CHOICES, default='desayuno')
    sequence           = models.PositiveIntegerField(default=1)
    is_active          = models.BooleanField(default=True)

    categoria_alimento = models.ForeignKey(
        CategoriaAlimento,
        on_delete=models.SET_NULL,
        related_name='alimentos_programados',
        null=True,
        blank=True
    )
    plan_nutricional   = models.ForeignKey(
        PlanNutricional,
        on_delete=models.SET_NULL,
        related_name='alimentos',
        null=True,
        blank=True
    )
    created_at         = models.DateTimeField(auto_now_add=True)
    updated_at         = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sequence']

    def __str__(self):
        return self.name

    @property
    def estimated_preparation_minutes(self):
        return round(float(self.portion_grams) / 30, 2)

    @property
    def has_sequence(self):
        return self.sequence > 0
