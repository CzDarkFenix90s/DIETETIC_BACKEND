# dietetic/views/paciente.py
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from dietetic.models import Paciente
from dietetic.serializers.paciente import PacienteSerializer
from dietetic.permissions import IsStaffOrReadOnly
from dietetic.pagination import StandardPagination


class PacienteViewSet(viewsets.ModelViewSet):
    queryset           = Paciente.objects.all()
    serializer_class   = PacienteSerializer
    pagination_class   = StandardPagination
    filterset_fields   = ['status']
    search_fields      = ['patient_code', 'full_name', 'goal']

    def get_permissions(self):
        if self.action in ['create', 'add_seguimiento']:
            # Permitir a cualquier usuario autenticado crear su perfil o añadir seguimientos
            return [permissions.IsAuthenticated()]
        return [IsStaffOrReadOnly()]

    @action(detail=True, methods=['post'], url_path='add-seguimiento')
    def add_seguimiento(self, request, pk=None):
        paciente = self.get_object()
        from dietetic.serializers.paciente import AddSeguimientoNutricionalSerializer
        from dietetic.models.paciente import SeguimientoNutricional
        
        serializer = AddSeguimientoNutricionalSerializer(data={'patient_id': paciente.id, **request.data})
        serializer.is_valid(raise_exception=True)
        
        seguimiento = SeguimientoNutricional.objects.create(
            paciente=paciente,
            weight_kg=serializer.validated_data['weight_kg'],
            waist_cm=serializer.validated_data.get('waist_cm'),
            notes=serializer.validated_data.get('notes', '')
        )
        
        # Actualizar el peso del paciente con el nuevo registro
        paciente.current_weight = seguimiento.weight_kg
        paciente.save(update_fields=['current_weight'])
        
        from dietetic.serializers.paciente import SeguimientoNutricionalSerializer
        return Response(SeguimientoNutricionalSerializer(seguimiento).data, status=status.HTTP_201_CREATED)

