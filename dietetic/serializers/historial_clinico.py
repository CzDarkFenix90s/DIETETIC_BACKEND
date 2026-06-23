from rest_framework import serializers
from dietetic.models import HistorialClinico


class HistorialClinicoSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(source='paciente', read_only=True)

    class Meta:
        model = HistorialClinico
        fields = [
            'id', 'paciente_id', 'alergias', 'enfermedades_cronicas',
            'antecedentes_familiares', 'medicamentos_actuales', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
