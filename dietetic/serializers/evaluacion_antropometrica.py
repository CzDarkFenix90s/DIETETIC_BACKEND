from rest_framework import serializers
from dietetic.models import EvaluacionAntropometrica


class EvaluacionAntropometricaSerializer(serializers.ModelSerializer):
    consulta_id = serializers.PrimaryKeyRelatedField(source='consulta', read_only=True)

    class Meta:
        model = EvaluacionAntropometrica
        fields = [
            'id', 'consulta_id', 'peso', 'altura', 'imc',
            'grasa_corporal_porcentaje', 'masa_muscular_kg', 'created_at'
        ]
        read_only_fields = ['id', 'imc', 'created_at']
