from rest_framework import viewsets, permissions
from dietetic.models import MomentoComida
from dietetic.serializers.momento_comida import MomentoComidaSerializer
from dietetic.permissions import IsStaffOrReadOnly


class MomentoComidaViewSet(viewsets.ModelViewSet):
    queryset = MomentoComida.objects.all()
    serializer_class = MomentoComidaSerializer
    filterset_fields = ['dia_plan']
    search_fields = ['nombre_momento']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsStaffOrReadOnly()]
        return [permissions.AllowAny()]
