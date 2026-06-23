from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from dietetic.models import SintomaDiario
from dietetic.serializers.sintoma_diario import SintomaDiarioSerializer
from dietetic.permissions import IsStaffOrReadOnly


class SintomaDiarioViewSet(viewsets.ModelViewSet):
    queryset = SintomaDiario.objects.all()
    serializer_class = SintomaDiarioSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['paciente', 'fecha', 'sintoma']
    search_fields = ['paciente__full_name', 'notas']
    ordering_fields = ['fecha', 'created_at']
    ordering = ['-fecha']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return SintomaDiario.objects.all()
        # Si es un paciente, solo ve sus propios registros
        if hasattr(user, 'paciente_profile'):
            return SintomaDiario.objects.filter(paciente=user.paciente_profile)
        return SintomaDiario.objects.none()
