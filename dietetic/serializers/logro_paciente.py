from rest_framework import serializers
from dietetic.models import LogroPaciente


class LogroPacienteSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(source='paciente', read_only=True)
    paciente_nombre = serializers.CharField(source='paciente.full_name', read_only=True)

    class Meta:
        model = LogroPaciente
        fields = ['id', 'paciente_id', 'paciente_nombre', 'nombre', 'descripcion', 'fecha_logro', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
