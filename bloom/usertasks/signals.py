from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Task

@receiver(post_save, sender=User)
def create_task_status_for_new_user(sender, instance, created, **kwargs):
    if created:
        Task.save_task_status(instance)
        Task.select_random_tasks(instance)
