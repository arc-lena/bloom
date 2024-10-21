from django.contrib.sessions.backends import file
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=Task)
def create_task_status_for_users(sender, instance, created, **kwargs):
    if created:
        # Створюємо TaskStatus для кожного користувача
        for user in User.objects.all():
            TaskStatus.objects.get_or_create(task=instance, user=user)


@receiver(post_save, sender=TaskStatus)
def update_user_level_on_task_completion(sender, instance, **kwargs):
    # Якщо завдання було завершено
    if instance.completed:
        profile =file.objects.get(user=instance.user)
        profile.completed_tasks_count += 1

        # Підвищення рівня після 3 виконаних завдань
        if profile.completed_tasks_count >= 3:
            profile.level += 1
            profile.completed_tasks_count = 0  # Скидаємо лічильник

        profile.save()
