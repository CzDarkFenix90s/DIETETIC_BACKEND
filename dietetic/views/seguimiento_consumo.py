from rest_framework import viewsets, permissions
from dietetic.models import SeguimientoConsumo
from dietetic.serializers.seguimiento_consumo import SeguimientoConsumoSerializer
from dietetic.permissions import IsStaffOrReadOnly


class SeguimientoConsumoViewSet(viewsets.ModelViewSet):
    queryset = SeguimientoConsumo.objects.all()
    serializer_class = SeguimientoConsumoSerializer
    filterset_fields = ['paciente', 'momento_comida', 'completado']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated()]
