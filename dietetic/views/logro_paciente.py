from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from dietetic.models import LogroPaciente
from dietetic.serializers.logro_paciente import LogroPacienteSerializer
from dietetic.permissions import IsStaffOrReadOnly


class LogroPacienteViewSet(viewsets.ModelViewSet):
    queryset = LogroPaciente.objects.all()
    serializer_class = LogroPacienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['paciente', 'fecha_logro']
    search_fields = ['paciente__full_name', 'nombre', 'descripcion']
    ordering_fields = ['fecha_logro', 'created_at']
    ordering = ['-fecha_logro']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return LogroPaciente.objects.all()
        if hasattr(user, 'paciente_profile'):
            return LogroPaciente.objects.filter(paciente=user.paciente_profile)
        return LogroPaciente.objects.none()
