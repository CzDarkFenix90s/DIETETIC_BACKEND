from rest_framework import viewsets, permissions
from dietetic.models import NotaConsulta
from dietetic.serializers.nota_consulta import NotaConsultaSerializer
from dietetic.permissions import IsStaffOrReadOnly


class NotaConsultaViewSet(viewsets.ModelViewSet):
    queryset = NotaConsulta.objects.all()
    serializer_class = NotaConsultaSerializer
    filterset_fields = ['consulta']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsStaffOrReadOnly()]
        return [permissions.AllowAny()]
