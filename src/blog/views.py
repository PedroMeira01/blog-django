from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Post, Keyword
from .serializers import UserSerializer, PostSerializer, KeywordSerializer
from .permissions import IsAuthenticatedOrUserCreateOnly, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication  # Importe a autenticação JWT

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrUserCreateOnly]

class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    authentication_classes = [JWTAuthentication]  # Use a autenticação JWT
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Aplica a permissão personalizada

