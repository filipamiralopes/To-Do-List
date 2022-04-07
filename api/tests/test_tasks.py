"""Test file for the task's list and detail endpoints."""

from django.urls import reverse
from rest_framework import status
from api.tests import base_test
from api.models import Task


class TaskTestCase(base_test.NewUserTestCase):
    """Tests for the /tasks list and detail endpoints."""

    def test_list_tasks(self) -> None:
        task = Task.objects.create(name="Train more orcs", creator=self.user)
        response = self.client.get(
            reverse("api:task-list"),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], task.name)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_task(self) -> None:
        task = Task.objects.create(name="Summon up the Nazgul", creator=self.user)
        response = self.client.get(
            reverse("api:task-detail", kwargs={"pk": task.id}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], task.id)

    def test_add_task(self) -> None:
        response = self.client.post(
            reverse("api:task-list"),
            data={"name": "Train more orcs"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task = Task.objects.first()
        self.assertEqual(response.data["id"], task.id)
        # Check task is created with default status
        self.assertEqual(response.data["status"], "IN_PROGRESS")
        # Check task belongs to (current) logged-in user
        self.assertIn(f"/users/{self.user.id}", response.data["creator"])

    def test_delete_task(self) -> None:
        task = Task.objects.create(name="Summon up the Nazgul", creator=self.user)
        response = self.client.delete(
            reverse("api:task-detail", kwargs={"pk": task.id}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Check that there are no tasks in the database
        self.assertEqual(Task.objects.count(), 0)

    def test_update_task_status(self) -> None:
        task = Task.objects.create(name="Summon up the Nazgul", creator=self.user)
        response = self.client.get(
            reverse("api:task-detail", kwargs={"pk": task.id}),
            format="json",
        )
        self.assertEqual(response.data["status"], "IN_PROGRESS")
        response = self.client.patch(
            reverse("api:task-detail", kwargs={"pk": task.id}),
            data={"status": "COMPLETED"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "COMPLETED")

    def test_filter_tasks_by_status(self) -> None:
        tasks = Task.objects.bulk_create([
            Task(name="Train more orcs", status="COMPLETED", creator=self.user),
            Task(name="Summon up the Nazgul", status="IN_PROGRESS", creator=self.user),
        ])
        response = self.client.get(
            reverse("api:task-list"),
            data={"status": "IN_PROGRESS"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], tasks[1].id)
        self.assertEqual(len(response.data), 1)
