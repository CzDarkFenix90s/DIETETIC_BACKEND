# dietetic/views/__init__.py
from .auth import RegisterView, LogoutView
from .health import health_check
from .plan_nutricional import PlanNutricionalViewSet
from .alimento_programado import AlimentoProgramadoViewSet
from .consulta_dietetica import ConsultaDieteticaViewSet
from .paciente import PacienteViewSet
from .nutricionista import NutricionistaViewSet
from .user import UserViewSet
from .preferencia_alimentaria import PreferenciaAlimentariaViewSet
from .objetivo_paciente import ObjetivoPacienteViewSet
from .logro_paciente import LogroPacienteViewSet
