from django.db import models
from django.contrib.auth.models import User  # Importar o modelo User padrão
from .keyword import Keyword

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Usar o modelo User padrão
    created_at = models.DateTimeField(auto_now_add=True)
    keywords = models.OneToOneField(Keyword, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title