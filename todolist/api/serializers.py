"""
Contains the django rest framework Task serializer, which is responsible for
serializing and deserializing the task instances into representations such as json.

Using Django ModelSerializer to abstract way this complexity.
"""

from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
