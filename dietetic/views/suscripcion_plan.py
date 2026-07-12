# dietetic/views/suscripcion_plan.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from dietetic.models.suscripcion_plan import SuscripcionPlan
from dietetic.serializers.suscripcion_plan import SuscripcionPlanSerializer
from dietetic.pagination import StandardPagination


class SuscripcionPlanViewSet(viewsets.ModelViewSet):
    serializer_class = SuscripcionPlanSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return SuscripcionPlan.objects.all()
        try:
            return SuscripcionPlan.objects.filter(paciente=user.paciente_profile)
        except AttributeError:
            return SuscripcionPlan.objects.none()
