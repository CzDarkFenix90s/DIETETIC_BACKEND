from rest_framework import serializers
from dietetic.models import RutinaEjercicio, PlanNutricional


class RutinaEjercicioSerializer(serializers.ModelSerializer):
    plan_nutricional = serializers.PrimaryKeyRelatedField(queryset=PlanNutricional.objects.all(), required=False)
    plan_nutricional_id = serializers.PrimaryKeyRelatedField(source='plan_nutricional', read_only=True)
    name = serializers.CharField(source='plan_nutricional.name', read_only=True)
    description = serializers.CharField(source='descripcion_rutina')
    difficulty = serializers.SerializerMethodField()
    duration_minutes = serializers.IntegerField(source='duracion_minutos')

    class Meta:
        model = RutinaEjercicio
        fields = [
            'id', 'plan_nutricional', 'plan_nutricional_id', 'name', 'description',
            'difficulty', 'duration_minutes', 'dias_semana',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_difficulty(self, obj):
        # Lógica simple: si dura más de 40 min es intensa
        if obj.duracion_minutos >= 40:
            return 'intensa'
        return 'media'

