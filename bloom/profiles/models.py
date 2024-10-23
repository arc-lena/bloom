from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    level = models.IntegerField(default=0)
    points_balance = models.IntegerField(default=0)
    completed_tasks_count = models.IntegerField(default=0)