from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Task, TaskStatus


@receiver(post_save, sender=User)
def create_task_status_for_new_user(sender, instance, created, **kwargs):
    if created:
        Task.save_task_status(instance)
        Task.select_random_tasks(instance)


@receiver(post_save, sender=TaskStatus)
def update_user_level_on_task_complete(sender, instance, **kwargs):
    if instance.completed:
        # Отримуємо профіль користувача
        profile = instance.user.profile  # Припустимо, що ви маєте зв'язок між TaskStatus і User через Profile
        profile.completed_tasks_count += 1  # Збільшуємо кількість виконаних завдань
        profile.level = profile.completed_tasks_count // 3  # Обчислюємо новий рівень
        profile.save()
