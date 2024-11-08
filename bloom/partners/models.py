import random
from django.db import models
from django.contrib.auth.models import User

class Partner(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField(blank=True, null=True) 
    image = models.ImageField(upload_to='partner_images/', blank=True, null=True)  
    points_required = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for user in User.objects.all():
            PartnerStatus.objects.get_or_create(user=user, partner=self)

    @staticmethod
    def new_user(user):
        for partner in Partner.objects.all():
            PartnerStatus.objects.get_or_create(user=user, partner=partner)

class Promocode(models.Model):
    promocode = models.CharField(max_length=50)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.partner.name} - {self.promocode}'

class PartnerStatus(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE) 
    status = models.CharField(max_length=50, default='not redeemed') 
    timestamp = models.DateTimeField(auto_now_add=True)
    promocode = models.CharField(max_length=50, blank=True, null=True)

    def redeem(self):
        promocodes = Promocode.objects.filter(partner=self.partner)
        if promocodes.exists():
            selected_promocode = random.choice(promocodes)
            self.promocode = selected_promocode.promocode
            selected_promocode.delete()
            self.status = 'redeemed'
            self.save()
            return True
     

    def __str__(self):
        return f'{self.user.username} - {self.partner.name} - {self.status}'