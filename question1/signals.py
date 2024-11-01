from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time
import datetime

@receiver(post_save, sender=User)
def sync_signal_receiver(sender, instance, **kwargs):
    print(f"Signal received at {datetime.datetime.now()}, starting delay...")
    time.sleep(5)  # Simulates a synchronous delay
    print(f"Signal processing complete at {datetime.datetime.now()}.")
