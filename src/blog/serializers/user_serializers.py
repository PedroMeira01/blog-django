# blog/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Adicione um campo para a senha

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')  # Remova a senha dos dados validados
        user = User(**validated_data)
        user.set_password(password)  # Configure a senha corretamente
        user.save()
        return user