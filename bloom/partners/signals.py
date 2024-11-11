from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Partner

@receiver(post_save, sender=User)
def create_partner_status_for_new_user(sender, instance, created, **kwargs):
    if created:
        Partner.new_user(instance)