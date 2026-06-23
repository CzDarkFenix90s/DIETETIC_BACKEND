import logging
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

logger = logging.getLogger(__name__)


def _send_email(subject, template_name, context, to_email):
    """
    Función privada para enviar correos con texto plano y HTML.
    """
    try:
        # Renderizar templates
        html_message = render_to_string(f'{template_name}.html', context)
        plain_message = strip_tags(html_message)
        
        # Crear y enviar el correo
        msg = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[to_email]
        )
        msg.attach_alternative(html_message, "text/html")
        msg.send(fail_silently=False)
        
        logger.info(f"Correo enviado exitosamente a {to_email}")
        return True
    except Exception as e:
        logger.error(f"Error al enviar correo a {to_email}: {str(e)}")
        return False


def send_welcome_email(user):
    """
    Envía un correo de bienvenida a un nuevo usuario.
    """
    subject = "¡Bienvenido a Dietética App!"
    context = {
        'user': user,
        'username': user.username,
    }
    return _send_email(subject, 'emails/welcome', context, user.email)


def send_password_reset_email(user, reset_url):
    """
    Envía un correo con el enlace para restablecer la contraseña.
    """
    subject = "Recuperación de Contraseña - Dietética App"
    context = {
        'user': user,
        'reset_url': reset_url,
    }
    return _send_email(subject, 'emails/password_reset', context, user.email)