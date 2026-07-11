# dietetic/serializers/nutricionista.py
from django.contrib.auth.models import User
from rest_framework import serializers

from dietetic.models import Nutricionista


class NutricionistaSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    fee_with_bonus = serializers.SerializerMethodField()
    is_experienced = serializers.SerializerMethodField()
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)

    class Meta:
        model = Nutricionista
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

    def create(self, validated_data):
        first_name = validated_data.get('first_name', '')
        last_name = validated_data.get('last_name', '')
        prof_id = validated_data.get('professional_id', '')

        username = f"nutri_{prof_id.lower().replace('-', '_')}"
        email = f"{username}@dietetic.com"

        user, _ = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'is_staff': True,
                'is_active': True,
            }
        )

        user.is_active = True
        user.set_password("Nutri123456*")
        user.save()

        from dietetic.models.user_profile import UserProfile
        profile, _ = UserProfile.objects.get_or_create(
            user=user,
            defaults={
                'role': 'NUTRICIONISTA',
                'is_verified': True,
            }
        )
        profile.is_verified = True
        profile.save()

        validated_data['user'] = user
        return super().create(validated_data)
