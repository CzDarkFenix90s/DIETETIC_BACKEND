from rest_framework import viewsets, permissions
from dietetic.models import DiaPlan
from dietetic.serializers.dia_plan import DiaPlanSerializer
from dietetic.permissions import IsStaffOrReadOnly


class DiaPlanViewSet(viewsets.ModelViewSet):
    queryset = DiaPlan.objects.all()
    serializer_class = DiaPlanSerializer
    filterset_fields = ['plan_nutricional']
    search_fields = ['nombre_dia']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsStaffOrReadOnly()]
        return [permissions.AllowAny()]
