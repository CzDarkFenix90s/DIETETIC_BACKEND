from rest_framework import viewsets, permissions
from dietetic.models import ProgresoFoto
from dietetic.serializers.progreso_fotos import ProgresoFotoSerializer

class ProgresoFotoViewSet(viewsets.ModelViewSet):
    queryset = ProgresoFoto.objects.all()
    serializer_class = ProgresoFotoSerializer
    filterset_fields = ['paciente']

    def get_permissions(self):
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ProgresoFoto.objects.all()
        if hasattr(user, 'paciente_profile'):
            return ProgresoFoto.objects.filter(paciente=user.paciente_profile)
        return ProgresoFoto.objects.none()

    def perform_create(self, serializer):
        if not self.request.user.is_staff and hasattr(self.request.user, 'paciente_profile'):
            serializer.save(paciente=self.request.user.paciente_profile)
        else:
            serializer.save()
