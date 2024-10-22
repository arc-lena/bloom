from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        for user in User.objects.all():
            TaskStatus.objects.get_or_create(task=self, user=user)

    def __str__(self):
        return self.title


class TaskStatus(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.user}) {self.task.title} - {'Completed' if self.completed else 'Not Completed'}"