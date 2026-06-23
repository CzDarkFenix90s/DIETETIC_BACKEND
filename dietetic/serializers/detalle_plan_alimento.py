from rest_framework import serializers
from dietetic.models import DetallePlanAlimento


class DetallePlanAlimentoSerializer(serializers.ModelSerializer):
    momento_comida_id = serializers.PrimaryKeyRelatedField(source='momento_comida', read_only=True)
    alimento_programado_id = serializers.PrimaryKeyRelatedField(source='alimento_programado', read_only=True)

    class Meta:
        model = DetallePlanAlimento
        fields = [
            'id', 'momento_comida_id', 'alimento_programado_id',
            'cantidad_gramos', 'orden', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
