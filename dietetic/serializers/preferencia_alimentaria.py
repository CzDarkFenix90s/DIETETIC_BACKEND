from rest_framework import serializers
from dietetic.models import PreferenciaAlimentaria


class PreferenciaAlimentariaSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(source='paciente', read_only=True)
    paciente_nombre = serializers.CharField(source='paciente.full_name', read_only=True)
    tipo_preferencia_display = serializers.CharField(source='get_tipo_preferencia_display', read_only=True)

    class Meta:
        model = PreferenciaAlimentaria
        fields = ['id', 'paciente_id', 'paciente_nombre', 'tipo_preferencia', 'tipo_preferencia_display', 'descripcion', 'fecha_registro', 'created_at', 'updated_at']
        read_only_fields = ['id', 'fecha_registro', 'created_at', 'updated_at']
