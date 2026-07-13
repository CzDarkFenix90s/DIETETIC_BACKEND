from rest_framework import serializers
from django.contrib.auth.models import User
from dietetic.models.paciente import Paciente


class RegisterSerializer(serializers.Serializer):
    username  = serializers.CharField(max_length=150)
    email     = serializers.EmailField()
    password  = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=150, required=False, default='')
    last_name = serializers.CharField(max_length=150, required=False, default='')

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('This username is already taken.')
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('This email is already registered.')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': 'Passwords do not match.'})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        first_name = validated_data.pop('first_name', '')
        last_name = validated_data.pop('last_name', '')

        user = User.objects.create_user(
            **validated_data,
            first_name=first_name,
            last_name=last_name
        )

        # Crear perfil de Paciente vinculándolo exactamente como Nutricionista
        Paciente.objects.get_or_create(
            user=user,
            defaults={
                'patient_code': f'PAC-{user.id:04d}',
                'first_name': user.first_name,
                'last_name': user.last_name,
                'status': 'activo'
            }
        )

        return user


class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model  = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'is_staff', 'is_active', 'date_joined', 'role'
        ]
        read_only_fields = ['id', 'date_joined']

    def get_role(self, obj):
        if obj.is_superuser:
            return 'admin'
        if hasattr(obj, 'nutricionista_profile'):
            return 'nutricionista'
        if hasattr(obj, 'paciente_profile'):
            return 'paciente'
        return 'paciente' # Default


class UserProfileSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    avatar_url = serializers.SerializerMethodField()
    avatar = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model  = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'avatar_url', 'avatar']
        read_only_fields = ['id']

    def get_role(self, obj):
        if obj.is_superuser:
            return 'admin'
        if hasattr(obj, 'nutricionista_profile'):
            return 'nutricionista'
        if hasattr(obj, 'paciente_profile'):
            return 'paciente'
        return 'paciente'
        
    def get_avatar_url(self, obj):
        if hasattr(obj, 'profile') and obj.profile.avatar:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.profile.avatar.url)
        return None

    def update(self, instance, validated_data):
        avatar = validated_data.pop('avatar', None)
        instance = super().update(instance, validated_data)
        
        if avatar is not None:
            from dietetic.models.user_profile import UserProfile
            profile, created = UserProfile.objects.get_or_create(user=instance)
            profile.avatar = avatar
            profile.save()
            
        return instance

    def validate_email(self, value):
        request = self.context.get('request')
        if User.objects.filter(email=value).exclude(pk=request.user.pk).exists():
            raise serializers.ValidationError('This email is already in use.')
        return value


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True)
    new_password     = serializers.CharField(min_length=8, write_only=True)
    new_password2    = serializers.CharField(write_only=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password is incorrect.')
        return value

    def validate(self, data):
        if data['new_password'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': 'Passwords do not match.'})
        return data
