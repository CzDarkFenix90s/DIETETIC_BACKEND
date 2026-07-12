from django.db import models
from .consulta_dietetica import ConsultaDietetica
from .suscripcion_plan import SuscripcionPlan


class FacturaPago(models.Model):
    ESTADO_PAGO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('anulado', 'Anulado')
    ]

    consulta = models.ForeignKey(
        ConsultaDietetica,
        on_delete=models.CASCADE,
        related_name='facturas_pago',
        null=True,
        blank=True
    )
    suscripcion = models.ForeignKey(
        SuscripcionPlan,
        on_delete=models.CASCADE,
        related_name='facturas_pago',
        null=True,
        blank=True
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
        rel = self.consulta if self.consulta else self.suscripcion
        return f'Factura {rel} - {self.estado_pago}'
