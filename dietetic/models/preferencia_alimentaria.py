from django.db import models
from .paciente import Paciente


class PreferenciaAlimentaria(models.Model):
    TIPO_PREFERENCIA_CHOICES = [
        ('VEGETARIANO', 'Vegetariano'),
        ('VEGANO', 'Vegano'),
        ('SIN_GLUTEN', 'Sin gluten'),
        ('SIN_LACTOSA', 'Sin lactosa'),
        ('ALERGIA_MARISCOS', 'Alergia a mariscos'),
        ('ALERGIA_NUECES', 'Alergia a frutos secos'),
        ('ALERGIA_HUEVOS', 'Alergia a huevos'),
        ('ALERGIA_SOJA', 'Alergia a soja'),
        ('LOW_CARB', 'Dieta baja en carbohidratos'),
        ('KETO', 'Dieta cetogénica'),
        ('MEDITERRANEA', 'Dieta mediterránea'),
        ('OTRO', 'Otro'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='preferencias_alimentarias')
    tipo_preferencia = models.CharField(max_length=30, choices=TIPO_PREFERENCIA_CHOICES)
    descripcion = models.TextField(blank=True, default='')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_registro']

    def __str__(self):
        return f'{self.paciente.full_name} - {self.get_tipo_preferencia_display()}'
