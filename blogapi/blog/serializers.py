# blog/serializers.py
from rest_framework import serializers
from .models import User, Post, Keyword

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['id', 'words_json']

class PostSerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'keywords']

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