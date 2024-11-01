from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction

class Command(BaseCommand):
    help = "Test Django signal transaction behavior"

    def handle(self, *args, **options):
        print("Starting transaction...")
        with transaction.atomic():
            print("Creating user instance...")
            User.objects.create(username="test_user_transaction")
            print("User creation complete.")
