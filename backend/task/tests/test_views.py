"""
File used to make view tests for task app.
"""
from django.test import TestCase
from task.models import Task
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse



CREATE_TASK_URL=reverse('task:create')


def create_task(**params):
    """Create and return a new task."""
    return Task.objects.create(**params)


class TestingTaskAppViews(TestCase):
    """Test the view of task app."""
    
    
    def setUp(self):
        self.client = APIClient()
    
    def test_create_task(self):
        """Test creating a task."""
        
        payload = {
            'name': 'Study English',
            'times': 2,
            'minutes_for_times': 50,
        }
        response = self.client.post(CREATE_TASK_URL, payload)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task = Task.objects.get(name=payload['name'])
        self.assertTrue(task.name, payload['name'])