from django.db import models
from .consulta_dietetica import ConsultaDietetica


class FacturaPago(models.Model):
    ESTADO_PAGO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('anulado', 'Anulado')
    ]

    consulta = models.ForeignKey(
        ConsultaDietetica,
        on_delete=models.CASCADE,
        related_name='facturas_pago'
    )
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(null=True, blank=True)
    estado_pago = models.CharField(
        max_length=20,
        choices=ESTADO_PAGO_CHOICES,
        default='pendiente'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Factura {self.consulta} - {self.estado_pago}'
