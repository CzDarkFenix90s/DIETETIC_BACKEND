from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from dietetic.models import HorarioNutricionista
from dietetic.serializers.horario_nutricionista import HorarioNutricionistaSerializer
from dietetic.permissions import IsStaffOrReadOnly


class HorarioNutricionistaViewSet(viewsets.ModelViewSet):
    queryset = HorarioNutricionista.objects.all()
    serializer_class = HorarioNutricionistaSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nutricionista', 'dia_semana', 'is_active']
    search_fields = ['nutricionista__full_name']
    ordering_fields = ['dia_semana', 'hora_inicio', 'created_at']
    ordering = ['dia_semana', 'hora_inicio']
