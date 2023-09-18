# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication

# from .models import Keyword
# from .serializers import KeywordSerializer

# class KeywordViewSet(viewsets.ModelViewSet):
#     queryset = Keyword.objects.all()
#     serializer_class = KeywordSerializer
#     authentication_classes = [JWTAuthentication]  # Use a autenticação JWT
#     permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar