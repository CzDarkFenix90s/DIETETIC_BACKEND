from rest_framework import serializers
from dietetic.models import DiaPlan


class DiaPlanSerializer(serializers.ModelSerializer):
    plan_nutricional_id = serializers.PrimaryKeyRelatedField(source='plan_nutricional', read_only=True)

    class Meta:
        model = DiaPlan
        fields = ['id', 'plan_nutricional', 'plan_nutricional_id', 'nombre_dia', 'orden', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
