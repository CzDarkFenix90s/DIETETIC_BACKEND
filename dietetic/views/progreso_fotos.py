from rest_framework import viewsets, permissions
from dietetic.models import ProgresoFoto
from dietetic.serializers.progreso_fotos import ProgresoFotoSerializer
from dietetic.permissions import IsStaffOrReadOnly


class ProgresoFotoViewSet(viewsets.ModelViewSet):
    queryset = ProgresoFoto.objects.all()
    serializer_class = ProgresoFotoSerializer
    filterset_fields = ['paciente']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated()]
