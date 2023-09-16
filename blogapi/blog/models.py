from django.db import models
from django.contrib.auth.models import User  # Importe o modelo User padrão

class Keyword(models.Model):
    words_json = models.JSONField()

    def __str__(self):
        return ', '.join(self.words_json) if self.words_json else ''

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Use o modelo User padrão
    created_at = models.DateTimeField(auto_now_add=True)
    keywords = models.OneToOneField(Keyword, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
