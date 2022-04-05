"""This file contains the endpoints of the To-do list app."""

from rest_framework import viewsets
from .models import Task
from django.contrib.auth.models import User
from .serializers import TaskSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Associates tasks with users. An additional field `creator` will be passed to the
        create method of the serializer, along with the rest of the validated data from the request.
        """
        serializer.save(creator=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions for user instances.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
