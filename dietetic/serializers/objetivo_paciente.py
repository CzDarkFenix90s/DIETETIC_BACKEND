from rest_framework import serializers
from dietetic.models import ObjetivoPaciente


class ObjetivoPacienteSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(source='paciente', read_only=True)
    paciente_nombre = serializers.CharField(source='paciente.full_name', read_only=True)
    objetivo_display = serializers.CharField(source='get_objetivo_display', read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = ObjetivoPaciente
        fields = ['id', 'paciente_id', 'paciente_nombre', 'objetivo', 'objetivo_display', 'fecha_inicio', 'fecha_meta', 'estado', 'estado_display', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
