from rest_framework import serializers
from dietetic.models import ProgresoFoto


class ProgresoFotoSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(source='paciente', read_only=True)

    class Meta:
        model = ProgresoFoto
        fields = ['id', 'paciente_id', 'foto', 'descripcion', 'fecha_subida']
        read_only_fields = ['id', 'fecha_subida']
