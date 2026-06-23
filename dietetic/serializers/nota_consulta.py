from rest_framework import serializers
from dietetic.models import NotaConsulta


class NotaConsultaSerializer(serializers.ModelSerializer):
    consulta_id = serializers.PrimaryKeyRelatedField(source='consulta', read_only=True)

    class Meta:
        model = NotaConsulta
        fields = ['id', 'consulta_id', 'diagnostico', 'observaciones', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
