from rest_framework import viewsets, permissions
from dietetic.models import CategoriaAlimento
from dietetic.serializers.categoria_alimento import CategoriaAlimentoSerializer
from dietetic.permissions import IsStaffOrReadOnly


class CategoriaAlimentoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaAlimento.objects.all()
    serializer_class = CategoriaAlimentoSerializer
    search_fields = ['name']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsStaffOrReadOnly()]
        return [permissions.AllowAny()]
