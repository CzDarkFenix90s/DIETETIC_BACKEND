from django.contrib import admin
from django.contrib.auth.models import User
from dietetic.models import (
    PlanNutricional, AlimentoProgramado, Nutricionista, Paciente, SeguimientoNutricional, ConsultaDietetica,
    CategoriaAlimento, DiaPlan, MomentoComida, DetallePlanAlimento, EvaluacionAntropometrica,
    NotaConsulta, HistorialClinico, SeguimientoConsumo, RegistroAgua, ProgresoFoto,
    RutinaEjercicio, MensajeChat, NotificacionPush, FacturaPago, UserProfile,
    HorarioNutricionista, SintomaDiario, RegistroEjercicio, PreferenciaAlimentaria,
    ObjetivoPaciente, LogroPaciente
)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Perfiles de usuario'


class UserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name']


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'role', 'created_at']
    list_filter = ['role']
    search_fields = ['user__username', 'user__email']


@admin.register(HorarioNutricionista)
class HorarioNutricionistaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nutricionista', 'dia_semana', 'hora_inicio', 'hora_fin', 'is_active']
    list_filter = ['nutricionista', 'dia_semana', 'is_active']


@admin.register(SintomaDiario)
class SintomaDiarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente', 'fecha', 'sintoma', 'created_at']
    list_filter = ['paciente', 'sintoma', 'fecha']
    search_fields = ['paciente__first_name', 'paciente__last_name', 'notas']


@admin.register(RegistroEjercicio)
class RegistroEjercicioAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente', 'rutina_ejercicio', 'fecha', 'completado']
    list_filter = ['paciente', 'rutina_ejercicio', 'completado', 'fecha']


@admin.register(PreferenciaAlimentaria)
class PreferenciaAlimentariaAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente', 'tipo_preferencia', 'fecha_registro']
    list_filter = ['paciente', 'tipo_preferencia']
    search_fields = ['paciente__first_name', 'paciente__last_name', 'descripcion']


@admin.register(ObjetivoPaciente)
class ObjetivoPacienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente', 'objetivo', 'estado', 'fecha_inicio', 'fecha_meta']
    list_filter = ['paciente', 'objetivo', 'estado']
    search_fields = ['paciente__first_name', 'paciente__last_name']


@admin.register(LogroPaciente)
class LogroPacienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente', 'nombre', 'fecha_logro']
    list_filter = ['paciente', 'fecha_logro']
    search_fields = ['paciente__first_name', 'paciente__last_name', 'nombre', 'descripcion']


@admin.register(PlanNutricional)
class PlanNutricionalAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name', 'goal', 'target_calories', 'duration_weeks', 'estimated_cost', 'is_active', 'created_at']
    list_filter   = ['is_active']
    search_fields = ['name', 'goal']


@admin.register(AlimentoProgramado)
class AlimentoProgramadoAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name', 'categoria_alimento', 'meal_type', 'portion_grams', 'sequence', 'is_active', 'plan_nutricional']
    list_filter   = ['is_active', 'meal_type', 'plan_nutricional', 'categoria_alimento']
    search_fields = ['name', 'description']
    list_editable = ['sequence', 'portion_grams', 'is_active']


@admin.register(Nutricionista)
class NutricionistaAdmin(admin.ModelAdmin):
    list_display  = ['id', 'first_name', 'last_name', 'professional_id', 'specialty', 'consultation_fee', 'is_active']
    list_filter   = ['is_active']
    search_fields = ['first_name', 'last_name', 'professional_id', 'specialty']
    list_editable = ['consultation_fee', 'is_active']


class SeguimientoNutricionalInline(admin.TabularInline):
    model  = SeguimientoNutricional
    extra  = 0
    fields = ['weight_kg', 'waist_cm', 'notes']


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display    = ['id', 'patient_code', 'first_name', 'last_name', 'age', 'goal', 'status', 'current_weight', 'created_at']
    list_filter     = ['status']
    search_fields   = ['patient_code', 'first_name', 'last_name']
    inlines         = [SeguimientoNutricionalInline]
    readonly_fields = ['created_at', 'updated_at']


@admin.register(ConsultaDietetica)
class ConsultaDieteticaAdmin(admin.ModelAdmin):
    list_display    = ['id', 'paciente', 'nutricionista', 'plan_nutricional', 'status', 'scheduled_time', 'created_at']
    list_filter     = ['status', 'plan_nutricional']
    search_fields   = ['paciente__first_name', 'paciente__last_name', 'nutricionista__last_name', 'plan_nutricional__name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(CategoriaAlimento)
class CategoriaAlimentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    search_fields = ['name']


@admin.register(DiaPlan)
class DiaPlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'plan_nutricional', 'nombre_dia', 'orden']
    list_filter = ['plan_nutricional']
    search_fields = ['nombre_dia']
    list_editable = ['orden']


@admin.register(MomentoComida)
class MomentoComidaAdmin(admin.ModelAdmin):
    list_display = ['id', 'dia_plan', 'nombre_momento', 'orden']
    list_filter = ['dia_plan']
    search_fields = ['nombre_momento']
    list_editable = ['orden']


@admin.register(DetallePlanAlimento)
class DetallePlanAlimentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'momento_comida', 'alimento_programado', 'cantidad_gramos', 'orden']
    list_filter = ['momento_comida']
    list_editable = ['orden']


@admin.register(EvaluacionAntropometrica)
class EvaluacionAntropometricaAdmin(admin.ModelAdmin):
    list_display = ['id', 'consulta', 'peso', 'altura', 'imc']
    list_filter = ['consulta']
    readonly_fields = ['imc']


@admin.register(NotaConsulta)
class NotaConsultaAdmin(admin.ModelAdmin):
    list_display = ['id', 'consulta', 'created_at']
    list_filter = ['consulta']


@admin.register(HistorialClinico)
class HistorialClinicoAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente', 'created_at']
    search_fields = ['paciente__first_name', 'paciente__last_name']


@admin.register(SeguimientoConsumo)
class SeguimientoConsumoAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente', 'momento_comida', 'fecha', 'completado']
    list_filter = ['paciente', 'completado']


@admin.register(RegistroAgua)
class RegistroAguaAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente', 'fecha', 'cantidad_ml']
    list_filter = ['paciente', 'fecha']


@admin.register(ProgresoFoto)
class ProgresoFotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente', 'fecha_subida']
    list_filter = ['paciente']


@admin.register(RutinaEjercicio)
class RutinaEjercicioAdmin(admin.ModelAdmin):
    list_display = ['id', 'plan_nutricional', 'descripcion_rutina', 'duracion_minutos']
    list_filter = ['plan_nutricional']


@admin.register(MensajeChat)
class MensajeChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'remitente', 'destinatario', 'timestamp', 'leido']
    list_filter = ['remitente', 'destinatario', 'leido']


@admin.register(NotificacionPush)
class NotificacionPushAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente', 'titulo', 'leido', 'fecha_envio']
    list_filter = ['paciente', 'leido']


@admin.register(FacturaPago)
class FacturaPagoAdmin(admin.ModelAdmin):
    list_display = ['id', 'consulta', 'monto', 'estado_pago', 'fecha_pago']
    list_filter = ['estado_pago']
