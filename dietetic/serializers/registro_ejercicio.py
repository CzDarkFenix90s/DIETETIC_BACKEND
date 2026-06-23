from rest_framework import serializers
from dietetic.models import RegistroEjercicio


class RegistroEjercicioSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(source='paciente', read_only=True)
    paciente_nombre = serializers.CharField(source='paciente.full_name', read_only=True)
    rutina_ejercicio_id = serializers.PrimaryKeyRelatedField(source='rutina_ejercicio', read_only=True)
    rutina_descripcion = serializers.CharField(source='rutina_ejercicio.descripcion_rutina', read_only=True)

    class Meta:
        model = RegistroEjercicio
        fields = ['id', 'paciente_id', 'paciente_nombre', 'rutina_ejercicio_id', 'rutina_descripcion', 'fecha', 'completado', 'notas', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
