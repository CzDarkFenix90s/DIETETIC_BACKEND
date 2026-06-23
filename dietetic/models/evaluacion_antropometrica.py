from django.db import models
from .consulta_dietetica import ConsultaDietetica


class EvaluacionAntropometrica(models.Model):
    consulta = models.ForeignKey(
        ConsultaDietetica,
        on_delete=models.CASCADE,
        related_name='evaluaciones_antropometricas'
    )
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    altura = models.DecimalField(max_digits=6, decimal_places=2)
    imc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grasa_corporal_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    masa_muscular_kg = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.peso and self.altura:
            altura_m = float(self.altura) / 100
            if altura_m > 0:
                self.imc = round(float(self.peso) / (altura_m ** 2), 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Evaluación {self.consulta} - IMC: {self.imc}'
