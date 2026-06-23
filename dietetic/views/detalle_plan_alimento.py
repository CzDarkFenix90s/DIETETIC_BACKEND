from rest_framework import viewsets, permissions
from dietetic.models import DetallePlanAlimento
from dietetic.serializers.detalle_plan_alimento import DetallePlanAlimentoSerializer
from dietetic.permissions import IsStaffOrReadOnly


class DetallePlanAlimentoViewSet(viewsets.ModelViewSet):
    queryset = DetallePlanAlimento.objects.all()
    serializer_class = DetallePlanAlimentoSerializer
    filterset_fields = ['momento_comida', 'alimento_programado']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsStaffOrReadOnly()]
        return [permissions.AllowAny()]
