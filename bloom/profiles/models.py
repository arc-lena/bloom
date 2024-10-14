from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)  # Поле location
    birth_date = models.DateField(null=True, blank=True)  # Поле birth_date

    def __str__(self):
        return f'{self.user.username} Profile'