from django.db import models
from django.contrib.auth.models import User
import random

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for user in User.objects.all():
            TaskStatus.objects.get_or_create(task=self, user=user)

    @staticmethod
    def get_random_tasks(user):
        task_statuses = TaskStatus.objects.filter(user=user, completed=False)
        tasks = [task_status.task for task_status in task_statuses]
        if not tasks:
            return []
        selected_tasks = random.sample(tasks, min(3, len(tasks)))
        return selected_tasks

    def __str__(self):
        return self.title

class TaskStatus(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def toggle_completion(self):
        self.completed = not self.completed
        self.save()

    def __str__(self):
        return f"({self.user}) {self.task.title} - {'Completed' if self.completed else 'Not Completed'}"
