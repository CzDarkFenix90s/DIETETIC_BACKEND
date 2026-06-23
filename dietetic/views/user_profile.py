from rest_framework import viewsets, permissions
from dietetic.models import UserProfile
from dietetic.serializers.user_profile import UserProfileSerializer
from dietetic.permissions import IsStaffOrReadOnly


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return UserProfile.objects.all()
        return UserProfile.objects.filter(user=user)
