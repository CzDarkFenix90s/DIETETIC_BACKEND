from rest_framework import viewsets, permissions
from dietetic.models import FacturaPago
from dietetic.serializers.factura_pago import FacturaPagoSerializer
from dietetic.permissions import IsStaffOrReadOnly


class FacturaPagoViewSet(viewsets.ModelViewSet):
    queryset = FacturaPago.objects.all()
    serializer_class = FacturaPagoSerializer
    filterset_fields = ['consulta', 'estado_pago']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsStaffOrReadOnly()]
        return [permissions.IsAuthenticated()]
