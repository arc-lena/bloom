from django.db import models
from django.contrib.auth.models import User

class Partner(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField(blank=True, null=True) 
    image = models.ImageField(upload_to='partner_images/', blank=True, null=True)  
    points_required = models.PositiveIntegerField() 
    def __str__(self):
        return self.name

class PointTransaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending') 
    timestamp = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f'{self.user.username} - {self.partner.name} - {self.status}'