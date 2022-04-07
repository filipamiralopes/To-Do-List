"""Test file for object level permissions."""

from django.urls import reverse
from rest_framework import status
from api.tests import base_test
from api.models import Task
from django.contrib.auth.models import User


class PermissionsTestCase(base_test.NewUserTestCase):
    """Test if a user should be allowed to act on a particular endpoint."""

    def test_only_logged_in_users_can_add_task(self) -> None:
        self.client.logout()
        response = self.client.post(
            reverse("api:task-list"),
            data={"name": "Train more orcs"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_creator_can_delete_task(self) -> None:
        task = Task.objects.create(name="Recover Ring One", creator=self.user)
        self.client.logout()
        saruman = User.objects.create_user(username="saruman",
                                           email="saruman@isengard.me",
                                           password=self.password)
        self.client.force_login(user=saruman)
        response = self.client.delete(
            reverse("api:task-detail", kwargs={"pk": task.id}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Check task was not deleted from the database
        self.assertEqual(Task.objects.count(), 1)
        # and user was added to the database
        response = self.client.get(
            reverse("api:user-list"),
            format="json",
        )
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[1]["id"], saruman.id)

    def test_only_creator_can_update_task(self) -> None:
        task = Task.objects.create(name="Recover Ring One", creator=self.user)
        response = self.client.get(
            reverse("api:task-detail", kwargs={"pk": task.id}),
            format="json",
        )
        self.assertEqual(response.data["status"], "IN_PROGRESS")
        self.client.logout()
        saruman = User.objects.create_user(username="saruman",
                                           email="saruman@isengard.me",
                                           password=self.password)
        self.client.force_login(user=saruman)
        response = self.client.patch(
            reverse("api:task-detail", kwargs={"pk": task.id}),
            data={"status": "COMPLETED"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Check status is still as originally set by creator
        response = self.client.get(
            reverse("api:task-detail", kwargs={"pk": task.id}),
            format="json",
        )
        self.assertEqual(response.data["status"], "IN_PROGRESS")

    def test_anyone_can_list_tasks(self) -> None:
        task = Task.objects.create(name="Recover Ring One", creator=self.user)
        self.client.logout()
        response = self.client.get(
            reverse("api:task-list"),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], task.id)
        self.assertIn(f"/users/{self.user.id}", response.data[0]["creator"])

    def test_anyone_can_list_users(self) -> None:
        self.client.logout()
        response = self.client.get(
            reverse("api:user-list"),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], self.user.id)
        self.assertEqual(len(response.data), 1)

    def test_anyone_can_retrieve_task(self) -> None:
        task = Task.objects.create(name="Recover Ring One", creator=self.user)
        self.client.logout()
        response = self.client.get(
            reverse("api:task-detail", kwargs={"pk": task.id}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], task.id)

    def test_anyone_can_retrieve_user(self) -> None:
        self.client.logout()
        response = self.client.get(
            reverse("api:user-detail", kwargs={"pk": self.user.id}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.user.id)
