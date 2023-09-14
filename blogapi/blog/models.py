from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        app_label = 'blog'

class Keyword(models.Model):
    words_json = models.JSONField()  # Um campo JSON para armazenar as palavras-chave

    def __str__(self):
        return ', '.join(self.words_json) if self.words_json else ''
        
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    keywords = models.OneToOneField(Keyword, on_delete=models.CASCADE, null=True, blank=True)  # Relação 1 para 1

    def __str__(self):
        return self.title
