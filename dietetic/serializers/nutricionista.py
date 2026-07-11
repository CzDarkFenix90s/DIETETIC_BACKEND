# dietetic/serializers/nutricionista.py
from rest_framework import serializers
from dietetic.models import Nutricionista


class NutricionistaSerializer(serializers.ModelSerializer):
    full_name        = serializers.SerializerMethodField()
    fee_with_bonus   = serializers.SerializerMethodField()
    is_experienced   = serializers.SerializerMethodField()
    user_id          = serializers.PrimaryKeyRelatedField(source='user', read_only=True)

    class Meta:
        model  = Nutricionista
        fields = [
            'id', 'user_id', 'first_name', 'last_name', 'full_name', 'professional_id',
            'specialty', 'consultation_fee', 'fee_with_bonus', 'consultations_completed',
            'is_experienced', 'is_active', 'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def get_full_name(self, obj):
        return obj.full_name

    def get_fee_with_bonus(self, obj):
        return obj.fee_with_bonus

    def get_is_experienced(self, obj):
        return obj.is_experienced
