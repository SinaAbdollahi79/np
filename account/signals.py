from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile


@receiver(post_save, sender=User)
def save_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
