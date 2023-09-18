# blog/serializers.py
from rest_framework import serializers
from ..models.post import Post
from ..models.post import Keyword
from .keyword_serializers import KeywordSerializer

class PostSerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer()

    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'created_at', 'keywords']

    def create(self, validated_data):
        keywords_data = validated_data.pop('keywords')
        post = Post.objects.create(**validated_data)

        keyword, _ = Keyword.objects.get_or_create(**keywords_data)
        post.keywords = keyword
        post.save()

        return post
    
    def update(self, instance, validated_data):
        keywords_data = validated_data.pop('keywords')
        
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()

        keyword, _ = Keyword.objects.get_or_create(**keywords_data)
        instance.keywords = keyword
        instance.save()

        return instance