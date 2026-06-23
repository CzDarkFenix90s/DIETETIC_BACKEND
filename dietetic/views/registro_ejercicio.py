from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from dietetic.models import RegistroEjercicio
from dietetic.serializers.registro_ejercicio import RegistroEjercicioSerializer
from dietetic.permissions import IsStaffOrReadOnly


class RegistroEjercicioViewSet(viewsets.ModelViewSet):
    queryset = RegistroEjercicio.objects.all()
    serializer_class = RegistroEjercicioSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['paciente', 'rutina_ejercicio', 'fecha', 'completado']
    search_fields = ['paciente__full_name', 'notas']
    ordering_fields = ['fecha', 'created_at']
    ordering = ['-fecha']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return RegistroEjercicio.objects.all()
        # Si es un paciente, solo ve sus propios registros
        if hasattr(user, 'paciente_profile'):
            return RegistroEjercicio.objects.filter(paciente=user.paciente_profile)
        return RegistroEjercicio.objects.none()
