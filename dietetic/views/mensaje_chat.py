from rest_framework import viewsets, permissions
from dietetic.models import MensajeChat
from dietetic.serializers.mensaje_chat import MensajeChatSerializer


class MensajeChatViewSet(viewsets.ModelViewSet):
    queryset = MensajeChat.objects.all()
    serializer_class = MensajeChatSerializer
    filterset_fields = ['remitente', 'destinatario', 'leido']

    def get_permissions(self):
        return [permissions.IsAuthenticated()]
