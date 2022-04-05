"""This file contains the endpoints of the To-do list app."""

from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed, added, edited and deleted.

    Django ViewSet is a useful abstraction that automatically provides `list`,
    `create`, `retrieve`, `update` and `destroy` actions.

    Note: using viewsets is less explicit than building the views individually.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status"]
