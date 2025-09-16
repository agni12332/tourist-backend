# api/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PanicAlert
from .utils import send_notification  # custom function to send FCM/Email/SMS

@receiver(post_save, sender=PanicAlert)
def notify_emergency_contacts(sender, instance, created, **kwargs):
    if created:
        send_notification(instance)
