from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from dietetic.models.paciente import Paciente
from dietetic.models.user_profile import UserProfile
from dietetic.services.email import send_welcome_email


@receiver(post_save, sender=User)
def handle_user_profile(sender, instance, created, **kwargs):
    """
    Crea un perfil de Paciente y un UserProfile para CUALQUIER usuario nuevo.
    """
    if created:
        # Crear UserProfile genérico
        role = 'PACIENTE'
        if instance.is_superuser: role = 'ADMIN'
        elif instance.is_staff:     role = 'NUTRICIONISTA'

        UserProfile.objects.get_or_create(
            user=instance,
            defaults={'role': role}
        )

        # Crear Paciente si no es staff
        if not instance.is_staff:
            Paciente.objects.get_or_create(
                user=instance,
                defaults={
                    'patient_code': f'PAC-{instance.id:04d}',
                    'first_name': instance.first_name,
                    'last_name': instance.last_name,
                    'age': 0,
                    'current_weight': 0.0,
                    'height_cm': 0.0
                }
            )
