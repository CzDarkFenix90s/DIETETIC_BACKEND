from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from dietetic.models import ObjetivoPaciente
from dietetic.serializers.objetivo_paciente import ObjetivoPacienteSerializer
from dietetic.permissions import IsStaffOrReadOnly


class ObjetivoPacienteViewSet(viewsets.ModelViewSet):
    queryset = ObjetivoPaciente.objects.all()
    serializer_class = ObjetivoPacienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['paciente', 'objetivo', 'estado']
    search_fields = ['paciente__full_name']
    ordering_fields = ['fecha_inicio', 'fecha_meta', 'created_at']
    ordering = ['-fecha_inicio']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ObjetivoPaciente.objects.all()
        if hasattr(user, 'paciente_profile'):
            return ObjetivoPaciente.objects.filter(paciente=user.paciente_profile)
        return ObjetivoPaciente.objects.none()
