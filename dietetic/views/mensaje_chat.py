from rest_framework import viewsets, permissions
from django.db.models import Q
from dietetic.models import MensajeChat
from dietetic.serializers.mensaje_chat import MensajeChatSerializer


class MensajeChatViewSet(viewsets.ModelViewSet):
    queryset = MensajeChat.objects.all()
    serializer_class = MensajeChatSerializer
    filterset_fields = ['remitente', 'destinatario', 'leido']

    def get_permissions(self):
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        # Un usuario solo ve mensajes donde es remitente o destinatario
        user = self.request.user
        return MensajeChat.objects.filter(Q(remitente=user) | Q(destinatario=user))

    def perform_create(self, serializer):
        # El remitente siempre es el usuario autenticado
        serializer.save(remitente=self.request.user)
