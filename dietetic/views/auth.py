# dietetic/views/auth.py
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

        # Generar código de verificación
        profile = user.profile
        code = profile.generate_verification_code()

        # Enviar correo
        send_verification_email(user, code)

        refresh = RefreshToken.for_user(user)
        return Response({
            'access':   str(refresh.access_token),
            'refresh':  str(refresh),
            'user_id':  user.id,
            'username': user.username,
            'email':    user.email,
            'is_staff': user.is_staff,
            'is_verified': profile.is_verified,
            'message':  'Código de verificación enviado a tu correo.'
        }, status=status.HTTP_201_CREATED)


class VerifyEmailView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        code = request.data.get('code')
        if not code:
            return Response({'error': 'El código es requerido.'}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        profile = user.profile

        if profile.verification_code == code:
            profile.is_verified = True
            profile.verification_code = None
            profile.save()
            return Response({'message': 'Correo verificado exitosamente.'}, status=status.HTTP_200_OK)

        return Response({'error': 'Código inválido.'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response(
                {'error': 'Refresh token is required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            RefreshToken(refresh_token).blacklist()
        except TokenError:
            return Response(
                {'error': 'Token is invalid or expired.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response({'message': 'Session closed successfully.'})


class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data['email']
        user = User.objects.get(email=email)
        
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        reset_url = f"http://localhost:3000/reset-password/{uidb64}/{token}/"
        send_password_reset_email(user, reset_url)
        
        return Response({
            'message': 'Se ha enviado un correo con instrucciones para restablecer tu contraseña.'
        }, status=status.HTTP_200_OK)


class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            'message': 'Tu contraseña ha sido restablecida exitosamente.'
        }, status=status.HTTP_200_OK)
