from rest_framework import serializers
from dietetic.models import HorarioNutricionista


class HorarioNutricionistaSerializer(serializers.ModelSerializer):
    nutricionista_id = serializers.PrimaryKeyRelatedField(source='nutricionista', read_only=True)
    nutricionista_nombre = serializers.CharField(source='nutricionista.full_name', read_only=True)

    class Meta:
        model = HorarioNutricionista
        fields = ['id', 'nutricionista_id', 'nutricionista_nombre', 'dia_semana', 'hora_inicio', 'hora_fin', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
