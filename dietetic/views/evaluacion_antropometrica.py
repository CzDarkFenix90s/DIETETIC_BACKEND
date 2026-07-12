import uuid
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from dietetic.models import EvaluacionAntropometrica, ConsultaDietetica, Paciente
from dietetic.serializers.evaluacion_antropometrica import EvaluacionAntropometricaSerializer


class EvaluacionAntropometricaViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionAntropometrica.objects.all()
    serializer_class = EvaluacionAntropometricaSerializer
    filterset_fields = ['consulta']

    def get_permissions(self):
        # Aseguramos que cualquier paciente autenticado pueda subir sus datos
        return [permissions.IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        user = request.user

        # 1. Asegurar Perfil de Paciente
        paciente, _ = Paciente.objects.get_or_create(
            user=user,
            defaults={
                'patient_code': f"PAC-{uuid.uuid4().hex[:6].upper()}",
                'first_name': user.username
            }
        )

        # 2. Buscar Consulta activa (Necesaria para la Tabla #7)
        consulta = ConsultaDietetica.objects.filter(paciente=paciente).order_by('-created_at').first()

        if not consulta:
            return Response(
                {'error': 'Primero debes activar un plan en la sección de Planes para registrar evaluaciones.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 3. Guardar con la consulta encontrada
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(consulta=consulta)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
