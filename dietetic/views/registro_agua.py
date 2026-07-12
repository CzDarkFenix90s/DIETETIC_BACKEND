import uuid
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from dietetic.models import RegistroAgua, Paciente
from dietetic.serializers.registro_agua import RegistroAguaSerializer


class RegistroAguaViewSet(viewsets.ModelViewSet):
    queryset = RegistroAgua.objects.all()
    serializer_class = RegistroAguaSerializer
    filterset_fields = ['paciente', 'fecha']

    def get_permissions(self):
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        user = self.request.user

        # BUSCADOR Y CREADOR AUTOMÁTICO DE PERFIL (Auto-Sanación de BD)
        paciente, created = Paciente.objects.get_or_create(
            user=user,
            defaults={
                'patient_code': f"PAC-{uuid.uuid4().hex[:6].upper()}",
                'first_name': user.username,
                'status': 'activo'
            }
        )

        serializer.save(paciente=paciente)
