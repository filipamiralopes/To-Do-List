"""
Contains the django rest framework Task serializer, which is responsible for
serializing and deserializing the task instances into representations such as json.

Using Django ModelSerializer to abstract way this complexity.
"""

from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.HyperlinkedRelatedField(view_name="api:user-detail", read_only=True)

    class Meta:
        model = Task
        fields = ["url", "id", "status", "name", "creator"]
        extra_kwargs = {'url': {'view_name': 'api:task-detail'}}


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["url", "id", "username", "email", "tasks"]
        extra_kwargs = {'url': {'view_name': 'api:user-detail'}}

    @staticmethod
    def get_tasks(obj: User):
        """
        Return list of tasks' names.
        """
        return obj.tasks.values_list("name", flat=True)
