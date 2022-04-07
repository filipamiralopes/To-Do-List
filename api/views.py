"""
This file contains the endpoints of the To-do list app.

Django ViewSet is a useful abstraction that automatically provides `list`,
    `create`, `retrieve`, `update` and `destroy` actions.

Note: using viewsets is less explicit than building the views individually.
"""

from rest_framework import viewsets
from .models import Task
from django.contrib.auth.models import User
from .serializers import TaskSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from .permissions import IsCreatorOrReadOnly


class TaskViewSet(viewsets.ModelViewSet):
    """
    Here are the Middle Earth tasks.
    You can view and filter them by status "In-progress" and "Completed".
    To be able to add a task (from the Task List), you must be part of this mythic world (aka login).
    Only the creator of the task is able to delete or update its task (by following the task url), otherwise the Ring would never be destroyed.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status"]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]

    def perform_create(self, serializer):
        """
        Associates tasks with users. An additional field `creator` will be passed to the
        create method of the serializer, along with the rest of the validated data from the request.
        """
        serializer.save(creator=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Here are the inhabitants (aka users) of the Middle Earth.
    You can list them (and check their burdens too, aka tasks) and retrieve one of them by following the url.
    And that's it. Only a powerful Admin (yes, more powerful than Sauron itself) can change or delete inhabitants.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
