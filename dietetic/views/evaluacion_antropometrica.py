from rest_framework import viewsets, permissions
from dietetic.models import EvaluacionAntropometrica
from dietetic.serializers.evaluacion_antropometrica import EvaluacionAntropometricaSerializer
from dietetic.permissions import IsStaffOrReadOnly


class EvaluacionAntropometricaViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionAntropometrica.objects.all()
    serializer_class = EvaluacionAntropometricaSerializer
    filterset_fields = ['consulta']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsStaffOrReadOnly()]
        return [permissions.AllowAny()]
