from django.db import models
from .nutricionista import Nutricionista


class HorarioNutricionista(models.Model):
    DIA_SEMANA_CHOICES = [
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    ]

    nutricionista = models.ForeignKey(Nutricionista, on_delete=models.CASCADE, related_name='horarios')
    dia_semana = models.CharField(max_length=3, choices=DIA_SEMANA_CHOICES)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['dia_semana', 'hora_inicio']
        unique_together = ['nutricionista', 'dia_semana', 'hora_inicio']

    def __str__(self):
        return f'{self.nutricionista.full_name} - {self.get_dia_semana_display()} {self.hora_inicio}-{self.hora_fin}'
