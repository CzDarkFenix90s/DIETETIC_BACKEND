from rest_framework import serializers
from dietetic.models import RegistroAgua


class RegistroAguaSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(source='paciente', read_only=True)

    class Meta:
        model = RegistroAgua
        fields = ['id', 'paciente_id', 'fecha', 'cantidad_ml', 'created_at']
        read_only_fields = ['id', 'created_at']
