from rest_framework import viewsets, permissions
from dietetic.models import NotificacionPush
from dietetic.serializers.notificacion_push import NotificacionPushSerializer
from dietetic.permissions import IsStaffOrReadOnly


class NotificacionPushViewSet(viewsets.ModelViewSet):
    queryset = NotificacionPush.objects.all()
    serializer_class = NotificacionPushSerializer
    filterset_fields = ['paciente', 'leido']

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            return [permissions.IsAuthenticated(), IsStaffOrReadOnly()]
        return [permissions.IsAuthenticated()]
