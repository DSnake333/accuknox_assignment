import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def thread_checking_receiver(sender, instance, **kwargs):
    print("Signal received in thread:", threading.current_thread().name)
