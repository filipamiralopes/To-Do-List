"""
Contains the django rest framework Task serializer, which is responsible for
serializing and deserializing the task instances into representations such as json.

Using Django ModelSerializer to abstract way this complexity.
"""

from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source="creator.username", read_only=True)

    class Meta:
        model = Task
        fields = ["id", "status", "name", "creator"]


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "tasks"]