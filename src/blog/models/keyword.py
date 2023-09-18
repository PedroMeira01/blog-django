from django.db import models
from django.contrib.auth.models import User  # Importe o modelo User padrão

class Keyword(models.Model):
    words_json = models.JSONField()

    def __str__(self):
        return ', '.join(self.words_json) if self.words_json else ''
