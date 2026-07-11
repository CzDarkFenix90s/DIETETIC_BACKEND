from rest_framework import serializers
from dietetic.models import MensajeChat
from django.contrib.auth.models import User


class MensajeChatSerializer(serializers.ModelSerializer):
    remitente_id = serializers.PrimaryKeyRelatedField(source='remitente', read_only=True)

    # Campo para escritura
    destinatario = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True
    )
    # Campo para lectura
    destinatario_id = serializers.PrimaryKeyRelatedField(source='destinatario', read_only=True)

    class Meta:
        model = MensajeChat
        fields = ['id', 'remitente_id', 'destinatario', 'destinatario_id', 'contenido', 'timestamp', 'leido']
        read_only_fields = ['id', 'timestamp']
