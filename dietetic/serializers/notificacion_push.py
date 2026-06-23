from rest_framework import serializers
from dietetic.models import NotificacionPush


class NotificacionPushSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(source='paciente', read_only=True)

    class Meta:
        model = NotificacionPush
        fields = ['id', 'paciente_id', 'titulo', 'mensaje', 'leido', 'fecha_envio']
        read_only_fields = ['id', 'fecha_envio']
