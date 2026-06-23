from rest_framework import viewsets, permissions
from dietetic.models import RegistroAgua
from dietetic.serializers.registro_agua import RegistroAguaSerializer
from dietetic.permissions import IsStaffOrReadOnly


class RegistroAguaViewSet(viewsets.ModelViewSet):
    queryset = RegistroAgua.objects.all()
    serializer_class = RegistroAguaSerializer
    filterset_fields = ['paciente', 'fecha']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated()]
