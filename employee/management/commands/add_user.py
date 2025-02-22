from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create a new superuser in the database."

    def add_arguments(self, parser):
        parser.add_argument(
            "--username", type=str, required=True, help="Username for the superuser"
        )
        parser.add_argument(
            "--password", type=str, required=True, help="Password for the superuser"
        )

    def handle(self, *args, **options):
        User = get_user_model()
        username = options.get("username")
        password = options.get("password")

        if not username:
            self.stdout.write(self.style.ERROR("Username is required."))
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.ERROR(f"User with username '{username}' already exists.")
            )
            return

        # Create superuser
        user = User.objects.create_superuser(
            username=username.lower(),
            is_staff=True,
            is_superuser=True,
            is_active=True,
            password=password,  # `create_superuser` will handle password hashing
        )

        self.stdout.write(
            self.style.SUCCESS(f"Superuser '{user.username}' created successfully!")
        )
