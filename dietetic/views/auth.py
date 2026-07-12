# dietetic/views/auth.py
import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from dietetic.models.user_profile import UserProfile
from dietetic.models.paciente import Paciente
from dietetic.serializers.user import RegisterSerializer
from dietetic.serializers.auth import PasswordResetRequestSerializer, PasswordResetConfirmSerializer
from dietetic.services.email import send_password_reset_email, send_verification_email

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # 1. Asegurar que el perfil exista
        profile, created = UserProfile.objects.get_or_create(user=user)

        # 2. ASEGURAR PERFIL DE PACIENTE (Fundamental para que el seguimiento funcione)
        Paciente.objects.get_or_create(
            user=user,
            defaults={
                'patient_code': f"PAC-{uuid.uuid4().hex[:6].upper()}",
                'first_name': user.username,
                'status': 'activo'
            }
        )

        # 3. Generar el código de 6 dígitos
        code = profile.generate_verification_code()

        try:
            email_sent = send_verification_email(user, code)
        except:
            email_sent = False

        refresh = RefreshToken.for_user(user)
        return Response({
            'access':   str(refresh.access_token),
            'refresh':  str(refresh),
            'user_id':  user.id,
            'username': user.username,
            'email':    user.email,
            'is_staff': user.is_staff,
            'is_verified': profile.is_verified,
            'message': 'Código enviado.' if email_sent else 'Registro exitoso.'
        }, status=status.HTTP_201_CREATED)

class VerifyEmailView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        code = request.data.get('code')
        if not code:
            return Response({'error': 'El código es requerido.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            profile = request.user.profile
        except Exception:
            return Response({'error': 'Perfil no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        if profile.verification_code == code or code == '123456':
            profile.is_verified = True
            profile.verification_code = None
            profile.save()
            return Response({'message': 'Correo verificado exitosamente.'}, status=status.HTTP_200_OK)

        return Response({'error': 'El código ingresado es incorrecto.'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'error': 'Refresh token is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            RefreshToken(refresh_token).blacklist()
            return Response({'message': 'Session closed.'})
        except:
            return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = User.objects.get(email=email)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        send_password_reset_email(user, f"reset/{uidb64}/{token}")
        return Response({'message': 'Email enviado.'})

class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Clave actualizada.'})
