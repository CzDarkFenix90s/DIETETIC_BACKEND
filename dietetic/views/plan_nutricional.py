import uuid
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from django.utils import timezone

from dietetic.models import PlanNutricional, Paciente, FacturaPago, ConsultaDietetica, Nutricionista
from dietetic.serializers.plan_nutricional import PlanNutricionalSerializer
from dietetic.permissions import IsStaffOrReadOnly
from dietetic.pagination import StandardPagination


class PlanNutricionalViewSet(viewsets.ModelViewSet):
    queryset           = PlanNutricional.objects.all()
    serializer_class   = PlanNutricionalSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['is_active']
    search_fields      = ['name', 'goal', 'description']
    ordering_fields    = ['name', 'created_at', 'estimated_cost']
    ordering           = ['name']

    def get_permissions(self):
        if self.action == 'adquirir_plan':
            from rest_framework.permissions import IsAuthenticated
            return [IsAuthenticated()]
        return super().get_permissions()

    @action(detail=True, methods=['post'], url_path='adquirir')
    def adquirir_plan(self, request, pk=None):
        try:
            plan = self.get_object()
        except:
            return Response({'error': 'Plan no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        user = request.user

        # 1. Asegurar Perfil de Paciente
        paciente, _ = Paciente.objects.get_or_create(
            user=user,
            defaults={
                'patient_code': f"PAC-{uuid.uuid4().hex[:6].upper()}",
                'first_name': user.username
            }
        )

        # 2. Buscar Nutricionista
        nutri = Nutricionista.objects.filter(is_active=True).first() or Nutricionista.objects.first()
        if not nutri:
            # Crear uno por defecto para que el sistema no muera
            nutri = Nutricionista.objects.create(
                first_name="Sistema",
                last_name="Dietetic",
                professional_id=f"ID-{uuid.uuid4().hex[:4].upper()}",
                specialty="General",
                consultation_fee=0.0
            )

        # 3. Crear Consulta (Puente)
        consulta = ConsultaDietetica.objects.create(
            paciente=paciente,
            nutricionista=nutri,
            plan_nutricional=plan,
            status='programada',
            scheduled_time=timezone.now(),
            estimated_end=timezone.now() + timezone.timedelta(hours=1)
        )

        # 4. Crear Factura
        factura = FacturaPago.objects.create(
            consulta=consulta,
            monto=plan.estimated_cost,
            estado_pago='pagado',
            fecha_pago=timezone.now()
        )

        return Response({
            'message': 'Plan activado correctamente',
            'id_consulta': consulta.id,
            'id_factura': factura.id
        }, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'], url_path='alimentos')
    def active_alimentos(self, request, pk=None):
        from dietetic.models import AlimentoProgramado
        from dietetic.serializers.alimento_programado import AlimentoResumenSerializer
        plan = self.get_object()
        qs   = plan.alimentos.filter(is_active=True).order_by('sequence')
        page = self.paginate_queryset(qs)
        if page is not None:
            return self.get_paginated_response(
                AlimentoResumenSerializer(page, many=True).data
            )
        return Response(AlimentoResumenSerializer(qs, many=True).data)
