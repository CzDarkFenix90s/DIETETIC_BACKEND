from django.db import models
from .paciente import Paciente


class SintomaDiario(models.Model):
    SINTOMA_CHOICES = [
        ('ANSIEDAD', 'Ansiedad'),
        ('CANSANCIO', 'Cansancio'),
        ('DOLOR_CABEZA', 'Dolor de cabeza'),
        ('BUENA_ENERGIA', 'Buena energía'),
        ('HAMBRE_EXCESIVA', 'Hambre excesiva'),
        ('SUEÑO_MALO', 'Mal sueño'),
        ('SUEÑO_BUENO', 'Buen sueño'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='sintomas_diarios')
    fecha = models.DateField()
    sintoma = models.CharField(max_length=20, choices=SINTOMA_CHOICES)
    notas = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha']
        unique_together = ['paciente', 'fecha']

    def __str__(self):
        return f'{self.paciente.full_name} - {self.fecha} - {self.get_sintoma_display()}'
