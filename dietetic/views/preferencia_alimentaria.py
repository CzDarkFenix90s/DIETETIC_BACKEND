from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from dietetic.models import PreferenciaAlimentaria
from dietetic.serializers.preferencia_alimentaria import PreferenciaAlimentariaSerializer
from dietetic.permissions import IsStaffOrReadOnly


class PreferenciaAlimentariaViewSet(viewsets.ModelViewSet):
    queryset = PreferenciaAlimentaria.objects.all()
    serializer_class = PreferenciaAlimentariaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['paciente', 'tipo_preferencia']
    search_fields = ['paciente__full_name', 'descripcion']
    ordering_fields = ['fecha_registro', 'created_at']
    ordering = ['-fecha_registro']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return PreferenciaAlimentaria.objects.all()
        if hasattr(user, 'paciente_profile'):
            return PreferenciaAlimentaria.objects.filter(paciente=user.paciente_profile)
        return PreferenciaAlimentaria.objects.none()
