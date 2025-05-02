from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from tasks.models import Task
from datetime import date

class BaseTaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.task = Task.objects.create(
            user=self.user,
            title='Sample Task',
            description='A task for testing.',
            due_date=date.today(),
            is_completed=False
        )
        self.client.login(username='testuser', password='password123')

class TaskModelTestCase(BaseTaskTestCase):
    def test_task_str_representation(self):
        self.assertEqual(str(self.task), 'Sample Task')

    def test_task_completion_flag(self):
        self.task.is_completed = True
        self.task.save()
        self.assertTrue(Task.objects.get(pk=self.task.pk).is_completed)

class TaskViewsTestCase(BaseTaskTestCase):
    def test_dashboard_view(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sample Task')

    def test_task_create(self):
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'Create this task.',
            'due_date': date.today(),
            'is_completed': False
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.filter(user=self.user).count(), 2)

    def test_task_edit(self):
        response = self.client.post(reverse('task_edit', args=[self.task.pk]), {
            'title': 'Updated Task',
            'description': 'Updated description.',
            'due_date': date.today(),
            'is_completed': True
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertTrue(self.task.is_completed)

    def test_task_delete(self):
        response = self.client.post(reverse('task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_task_status_view(self):
        response = self.client.get(reverse('task_status'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sample Task')