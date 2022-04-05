"""The Task model is used to store all the tasks."""

from django.db import models


class Task(models.Model):

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    STATUS_CHOICES = ((IN_PROGRESS, 'In-progress'), (COMPLETED, 'Completed'))

    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default=IN_PROGRESS)
    name = models.TextField()

    def __str__(self):
        return self.name

