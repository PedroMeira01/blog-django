# blog/serializers.py
from rest_framework import serializers
from ..models.keyword import Keyword

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['words_json']