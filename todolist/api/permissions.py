"""This file set customs permissions for the users of the to-do list app."""

from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow creators of an object to edit it.
    Other users have read only rights.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any user/ request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write and Delete permissions are only allowed to the creator of the task
        return obj.creator == request.user
