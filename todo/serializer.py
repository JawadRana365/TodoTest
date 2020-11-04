from rest_framework import serializers
from .models import User,Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userName', 'password')

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'details', 'date')