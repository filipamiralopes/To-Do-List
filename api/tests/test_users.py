"""Test file for the users's list and detail endpoints."""

from django.urls import reverse
from rest_framework import status
from api.tests import base_test


class UserTestCase(base_test.NewUserTestCase):
    """Tests for the /users list and detail endpoints."""

    def test_list_users(self) -> None:
        response = self.client.get(
            reverse("api:user-list"),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["username"], self.user.username)
        self.assertEqual(response.data[0]["email"], self.user.email)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_user(self) -> None:
        response = self.client.get(
            reverse("api:user-detail", kwargs={"pk": self.user.id}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.user.username)
