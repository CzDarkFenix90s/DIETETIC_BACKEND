# dietetic/serializers/auth.py
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()


class CustomTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email']    = user.email
        token['is_staff'] = user.is_staff

        # Agregar is_verified al token
        if hasattr(user, 'profile'):
            token['is_verified'] = user.profile.is_verified
        else:
            token['is_verified'] = False

        # Determinar rol
        if user.is_superuser:
            token['role'] = 'admin'
        elif hasattr(user, 'nutricionista_profile'):
            token['role'] = 'nutricionista'
        else:
            token['role'] = 'paciente'

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id']  = self.user.id
        data['username'] = self.user.username
        data['email']    = self.user.email
        data['is_staff'] = self.user.is_staff

        # Agregar is_verified a la respuesta
        if hasattr(self.user, 'profile'):
            data['is_verified'] = self.user.profile.is_verified
        else:
            data['is_verified'] = False

        # Determinar rol para el frontend
        if self.user.is_superuser:
            data['role'] = 'admin'
        elif hasattr(self.user, 'nutricionista_profile'):
            data['role'] = 'nutricionista'
        else:
            data['role'] = 'paciente'

        return data


class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("No existe un usuario con este correo.")
        return value


class PasswordResetConfirmSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, min_length=8)
    new_password_confirm = serializers.CharField(write_only=True, min_length=8)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        
        try:
            uid = force_str(urlsafe_base64_decode(attrs['uidb64']))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError({"uidb64": "El enlace es inválido o ha expirado."})
        
        if not default_token_generator.check_token(user, attrs['token']):
            raise serializers.ValidationError({"token": "El enlace es inválido o ha expirado."})
        
        attrs['user'] = user
        return attrs

    def save(self):
        user = self.validated_data['user']
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
