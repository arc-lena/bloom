from celery import shared_task
from django.contrib.auth.models import User
from .models import Task
import logging


logger = logging.getLogger(__name__)

@shared_task
def daily_task_selection():
    logger.info("Running daily_task_selection")
    for user in User.objects.all():
        Task.select_random_tasks(user=user)
        logger.info(f"Selected tasks for user: {user.username}")