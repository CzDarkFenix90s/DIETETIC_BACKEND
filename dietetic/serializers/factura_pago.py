from rest_framework import serializers
from dietetic.models import FacturaPago


class FacturaPagoSerializer(serializers.ModelSerializer):
    consulta_id = serializers.PrimaryKeyRelatedField(source='consulta', read_only=True)
    suscripcion_id = serializers.PrimaryKeyRelatedField(source='suscripcion', read_only=True)

    class Meta:
        model = FacturaPago
        fields = ['id', 'consulta_id', 'suscripcion_id', 'monto', 'fecha_pago', 'estado_pago', 'created_at']
        read_only_fields = ['id', 'created_at']
