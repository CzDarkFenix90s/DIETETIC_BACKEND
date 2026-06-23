from rest_framework import viewsets, permissions
from dietetic.models import RutinaEjercicio
from dietetic.serializers.rutina_ejercicio import RutinaEjercicioSerializer
from dietetic.permissions import IsStaffOrReadOnly


class RutinaEjercicioViewSet(viewsets.ModelViewSet):
    queryset = RutinaEjercicio.objects.all()
    serializer_class = RutinaEjercicioSerializer
    filterset_fields = ['plan_nutricional']
    search_fields = ['descripcion_rutina']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsStaffOrReadOnly()]
        return [permissions.AllowAny()]
