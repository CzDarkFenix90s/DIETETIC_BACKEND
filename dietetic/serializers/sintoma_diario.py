from rest_framework import serializers
from dietetic.models import SintomaDiario


class SintomaDiarioSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(source='paciente', read_only=True)
    paciente_nombre = serializers.CharField(source='paciente.full_name', read_only=True)

    class Meta:
        model = SintomaDiario
        fields = ['id', 'paciente_id', 'paciente_nombre', 'fecha', 'sintoma', 'notas', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
