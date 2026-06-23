from rest_framework import viewsets, permissions
from dietetic.models import HistorialClinico
from dietetic.serializers.historial_clinico import HistorialClinicoSerializer
from dietetic.permissions import IsStaffOrReadOnly


class HistorialClinicoViewSet(viewsets.ModelViewSet):
    queryset = HistorialClinico.objects.all()
    serializer_class = HistorialClinicoSerializer
    filterset_fields = ['paciente']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsStaffOrReadOnly()]
        return [permissions.IsAuthenticated()]
