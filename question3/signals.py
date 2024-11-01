from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def transaction_check_receiver(sender, instance, **kwargs):
    print("Signal received; in transaction:", transaction.get_connection().in_atomic_block)
