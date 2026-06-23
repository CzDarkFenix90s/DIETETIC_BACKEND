from rest_framework import serializers
from dietetic.models import SeguimientoConsumo


class SeguimientoConsumoSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(source='paciente', read_only=True)
    momento_comida_id = serializers.PrimaryKeyRelatedField(source='momento_comida', read_only=True)

    class Meta:
        model = SeguimientoConsumo
        fields = [
            'id', 'paciente_id', 'momento_comida_id', 'fecha', 'completado', 'notas', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
