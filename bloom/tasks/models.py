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
    def select_random_tasks(user):
        TaskStatus.objects.filter(user=user).update(selected=False)

        task_statuses = TaskStatus.objects.filter(user=user, completed=False)
        tasks = [task_status.task for task_status in task_statuses]
        selected_tasks = random.sample(tasks, min(3, len(tasks)))
        for task in selected_tasks:
            TaskStatus.objects.filter(task=task, user=user).update(selected=True)

    @staticmethod
    def save_task_status(user):
        tasks = Task.objects.all()
        for task in tasks:
            TaskStatus.objects.get_or_create(task=task, user=user)

    def __str__(self):
        return self.title


class TaskStatus(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    selected = models.BooleanField(default=False)

    def toggle_completion(self):
        self.completed = not self.completed
        self.save()

    def __str__(self):
        return f"({self.user}) {self.task.title} - {'Completed' if self.completed else 'Not Completed'}"