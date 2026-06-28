from django.db import models
from .paciente import Paciente


class ObjetivoPaciente(models.Model):
    OBJETIVO_CHOICES = [
        ('BAJAR_PESO', 'Bajar peso'),
        ('GANAR_MASA', 'Ganar masa muscular'),
        ('MANTENER_PESO', 'Mantener peso'),
        ('REDUCIR_GRASA', 'Reducir grasa corporal'),
        ('MEJORAR_SALUD', 'Mejorar salud general'),
        ('MEJORAR_RENDIMIENTO', 'Mejorar rendimiento deportivo'),
        ('OTRO', 'Otro'),
    ]

    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROGRESO', 'En progreso'),
        ('CUMPLIDO', 'Cumplido'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='objetivos')
    objetivo = models.CharField(max_length=30, choices=OBJETIVO_CHOICES)
    fecha_inicio = models.DateField()
    fecha_meta = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f'{self.paciente.full_name} - {self.get_objetivo_display()} ({self.get_estado_display()})'
