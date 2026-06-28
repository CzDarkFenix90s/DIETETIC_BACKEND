# dietetic/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from dietetic.views.health      import health_check
from dietetic.views.auth        import RegisterView, LogoutView, PasswordResetRequestView, PasswordResetConfirmView
from dietetic.views.user                import UserViewSet
from dietetic.views.plan_nutricional    import PlanNutricionalViewSet
from dietetic.views.alimento_programado import AlimentoProgramadoViewSet
from dietetic.views.consulta_dietetica  import ConsultaDieteticaViewSet
from dietetic.views.paciente            import PacienteViewSet
from dietetic.views.nutricionista       import NutricionistaViewSet
from dietetic.views.categoria_alimento import CategoriaAlimentoViewSet
from dietetic.views.dia_plan import DiaPlanViewSet
from dietetic.views.momento_comida import MomentoComidaViewSet
from dietetic.views.detalle_plan_alimento import DetallePlanAlimentoViewSet
from dietetic.views.evaluacion_antropometrica import EvaluacionAntropometricaViewSet
from dietetic.views.nota_consulta import NotaConsultaViewSet
from dietetic.views.historial_clinico import HistorialClinicoViewSet
from dietetic.views.seguimiento_consumo import SeguimientoConsumoViewSet
from dietetic.views.registro_agua import RegistroAguaViewSet
from dietetic.views.progreso_fotos import ProgresoFotoViewSet
from dietetic.views.rutina_ejercicio import RutinaEjercicioViewSet
from dietetic.views.mensaje_chat import MensajeChatViewSet
from dietetic.views.notificacion_push import NotificacionPushViewSet
from dietetic.views.factura_pago import FacturaPagoViewSet
from dietetic.views.user_profile import UserProfileViewSet
from dietetic.views.horario_nutricionista import HorarioNutricionistaViewSet
from dietetic.views.sintoma_diario import SintomaDiarioViewSet
from dietetic.views.registro_ejercicio import RegistroEjercicioViewSet
from dietetic.views.preferencia_alimentaria import PreferenciaAlimentariaViewSet
from dietetic.views.objetivo_paciente import ObjetivoPacienteViewSet
from dietetic.views.logro_paciente import LogroPacienteViewSet
from dietetic.serializers.auth          import CustomTokenView

router = DefaultRouter()
router.register('users',           UserViewSet,                 basename='user')
router.register('profiles',        UserProfileViewSet,          basename='user-profile')
router.register('pacientes',       PacienteViewSet,             basename='paciente')
router.register('nutricionistas',  NutricionistaViewSet,        basename='nutricionista')
router.register('horarios-nutricionista', HorarioNutricionistaViewSet, basename='horario-nutricionista')
router.register('planes',          PlanNutricionalViewSet,      basename='plan-nutricional')
router.register('dias-plan',       DiaPlanViewSet,              basename='dia-plan')
router.register('momentos-comida', MomentoComidaViewSet,        basename='momento-comida')
router.register('categorias-alimentos', CategoriaAlimentoViewSet, basename='categoria-alimento')
router.register('alimentos',       AlimentoProgramadoViewSet,   basename='alimento')
router.register('detalles-alimentos-plan', DetallePlanAlimentoViewSet, basename='detalle-plan-alimento')
router.register('consultas',       ConsultaDieteticaViewSet,    basename='consulta')
router.register('notas-consulta',  NotaConsultaViewSet,         basename='nota-consulta')
router.register('historiales-clinicos', HistorialClinicoViewSet, basename='historial-clinico')
router.register('evaluaciones-antropometricas', EvaluacionAntropometricaViewSet, basename='evaluacion-antropometrica')
router.register('progresos-fotos', ProgresoFotoViewSet,         basename='progreso-foto')
router.register('rutinas-ejercicio', RutinaEjercicioViewSet,    basename='rutina-ejercicio')
router.register('registros-ejercicio', RegistroEjercicioViewSet, basename='registro-ejercicio')
router.register('sintomas-diarios', SintomaDiarioViewSet,        basename='sintoma-diario')
router.register('preferencias-alimentarias', PreferenciaAlimentariaViewSet, basename='preferencia-alimentaria')
router.register('objetivos-paciente', ObjetivoPacienteViewSet, basename='objetivo-paciente')
router.register('logros-paciente', LogroPacienteViewSet, basename='logro-paciente')
router.register('seguimientos-consumo', SeguimientoConsumoViewSet, basename='seguimiento-consumo')
router.register('registros-agua',  RegistroAguaViewSet,         basename='registro-agua')
router.register('mensajes-chat',   MensajeChatViewSet,          basename='mensaje-chat')
router.register('notificaciones-push', NotificacionPushViewSet, basename='notificacion-push')
router.register('facturas-pago',   FacturaPagoViewSet,          basename='factura-pago')

urlpatterns = [
    path('health/',             health_check),
    path('auth/register/',      RegisterView.as_view(), name='register'),
    path('auth/login/',         CustomTokenView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/',  TokenVerifyView.as_view()),
    path('auth/logout/',        LogoutView.as_view()),
    path('auth/password-reset/request/',  PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('auth/password-reset/confirm/',  PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('', include(router.urls)),
]
