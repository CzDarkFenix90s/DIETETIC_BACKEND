from rest_framework import serializers
from dietetic.models import MomentoComida


class MomentoComidaSerializer(serializers.ModelSerializer):
    dia_plan_id = serializers.PrimaryKeyRelatedField(source='dia_plan', read_only=True)

    class Meta:
        model = MomentoComida
        fields = ['id', 'dia_plan', 'dia_plan_id', 'nombre_momento', 'orden', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
