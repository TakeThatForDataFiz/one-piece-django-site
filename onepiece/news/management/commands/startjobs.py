from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Function that will add parsing details for API Request
        print("It Works")
