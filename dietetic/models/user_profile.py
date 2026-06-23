import uuid
from django.db import models
from django.contrib.auth.models import User


def user_avatar_path(instance, filename):
    """Ruta dinámica para guardar avatares: media/avatars/user_{id}/{uuid}{ext}"""
    ext = filename.split('.')[-1]
    return f'avatars/user_{instance.user.id}/{uuid.uuid4()}.{ext}'


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('NUTRICIONISTA', 'Nutricionista'),
        ('PACIENTE', 'Paciente'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='PACIENTE')
    avatar = models.ImageField(upload_to=user_avatar_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} - {self.role}'
