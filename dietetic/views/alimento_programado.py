# dietetic/views/alimento_programado.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg, Max, Min, Count

from dietetic.models import AlimentoProgramado
from dietetic.serializers.alimento_programado import AlimentoProgramadoSerializer, AlimentoResumenSerializer
from dietetic.permissions import IsStaffOrReadOnly
from dietetic.pagination import StandardPagination


class AlimentoProgramadoViewSet(viewsets.ModelViewSet):
    queryset           = AlimentoProgramado.objects.select_related('plan_nutricional', 'categoria_alimento').all()
    serializer_class   = AlimentoProgramadoSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['is_active', 'plan_nutricional', 'meal_type', 'categoria_alimento']
    search_fields      = ['name', 'description', 'plan_nutricional__name', 'categoria_alimento__name']
    ordering_fields    = ['name', 'portion_grams', 'sequence', 'created_at']
    ordering           = ['sequence']

    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsAdminUser],
        url_path='update-order',
    )
    def update_order(self, request, pk=None):
        alimento = self.get_object()
        try:
            sequence = int(request.data.get('sequence', 0))
            if sequence <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return Response(
                {'error': 'La secuencia debe ser un entero positivo.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        alimento.sequence = sequence
        alimento.save(update_fields=['sequence'])
        return Response({
            'id':           alimento.id,
            'name':         alimento.name,
            'new_sequence': alimento.sequence,
        })

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[AllowAny],
        url_path='available',
    )
    def available(self, request):
        qs   = self.filter_queryset(self.get_queryset().filter(is_active=True))
        page = self.paginate_queryset(qs)
        if page is not None:
            return self.get_paginated_response(
                AlimentoResumenSerializer(page, many=True).data
            )
        return Response(AlimentoResumenSerializer(qs, many=True).data)

    @action(
        detail=False,
        methods=['get'],
        url_path='stats',
    )
    def stats(self, request):
        qs     = AlimentoProgramado.objects.all()
        active = qs.filter(is_active=True)
        data   = active.aggregate(
            total_active = Count('id'),
            avg_portion_grams = Avg('portion_grams'),
            max_portion_grams = Max('portion_grams'),
            min_portion_grams = Min('portion_grams'),
        )
        data['total_inactive'] = qs.filter(is_active=False).count()
        if data['avg_portion_grams']:
            data['avg_portion_grams'] = round(float(data['avg_portion_grams']), 2)
        return Response(data)
