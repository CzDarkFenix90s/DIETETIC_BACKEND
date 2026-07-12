# dietetic/serializers/suscripcion_plan.py
from rest_framework import serializers
from dietetic.models.suscripcion_plan import SuscripcionPlan


class SuscripcionPlanSerializer(serializers.ModelSerializer):
    plan_name = serializers.CharField(source='plan.name', read_only=True)
    paciente_name = serializers.CharField(source='paciente.full_name', read_only=True)

    class Meta:
        model = SuscripcionPlan
        fields = [
            'id', 'paciente', 'paciente_name', 'plan', 'plan_name',
            'fecha_inicio', 'fecha_fin', 'estado', 'monto_pagado'
        ]
        read_only_fields = ['id', 'fecha_inicio']
