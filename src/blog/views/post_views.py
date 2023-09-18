from rest_framework import viewsets

from ..models.post import Post
from ..serializers.post_serializers import PostSerializer
from ..permissions import IsAuthenticatedOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]  # Aplica a permissão personalizada