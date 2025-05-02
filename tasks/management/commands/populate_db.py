import json
import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management import call_command
from django.conf import settings
from django.db import transaction
from tasks.models import Task
from users.models import Profile

class Command(BaseCommand):
    help = 'Clears the database and populates it with initial data (one user, profile, and tasks from a JSON fixture)'

    def handle(self, *args, **kwargs):
        # Prevent running in production
        if not settings.DEBUG:
            self.stdout.write(self.style.ERROR('This command can only run in DEBUG mode'))
            return

        # Clear the database (delete all users, profiles, and tasks)
        self.stdout.write(self.style.WARNING('Clearing existing users, profiles, and tasks...'))
        with transaction.atomic():
            User.objects.all().delete()
            Task.objects.all().delete()
            Profile.objects.all().delete()


        self.stdout.write('Creating user...')
        with transaction.atomic():
            user = User.objects.create_user(
                username='testuser',
                password='password123',
                email='testuser@example.com'
            )
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Created user: testuser (password: password123, id: {user.id})'))

            self.stdout.write('Creating user profile...')
            Profile.objects.create(
                user=user,
                profile_picture='profile_pics/default.jpg'
            )
            self.stdout.write(self.style.SUCCESS('Created profile for testuser'))

        # Load and modify the JSON fixture to set the correct user ID
        self.stdout.write('Loading tasks from JSON fixture...')
        fixture_path = os.path.join(settings.BASE_DIR, 'tasks', 'fixtures', 'tasks_fixture.json')
        try:
            with open(fixture_path, 'r') as f:
                fixture_data = json.load(f)
            for item in fixture_data:
                if item['model'] == 'tasks.task':
                    item['fields']['user'] = user.id

            temp_fixture_path = os.path.join(settings.BASE_DIR, 'tasks', 'fixtures', 'temp_tasks_fixture.json')
            with open(temp_fixture_path, 'w') as f:
                json.dump(fixture_data, f)

            # Load the modified fixture
            call_command('loaddata', temp_fixture_path, verbosity=0)
            self.stdout.write(self.style.SUCCESS('Successfully loaded tasks'))

            os.remove(temp_fixture_path)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to load JSON fixture: {e}'))
            return

        # Verify and summarize seeded data
        user_count = User.objects.count()
        profile_count = Profile.objects.count()
        task_count = Task.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f'Database seeded successfully: {user_count} user(s), {profile_count} profile(s), {task_count} task(s)'
        ))