from rest_framework import viewsets

from django.contrib.auth.models import User
from ..serializers.user_serializers import UserSerializer
from ..permissions import IsAuthenticatedOrUserCreateOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrUserCreateOnly]