from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import time

class Command(BaseCommand):
    help = "Test Django signal synchronous behavior"

    def handle(self, *args, **options):
        print("Creating user instance...")
        User.objects.create(username="test_user_command")
        print("User creation complete.")
