"""
File used to make view tests for task app.
"""
from django.test import TestCase
from task.models import Task
from rest_framework.test import APIClient
from rest_framework import status



def create_task(**params):
    """Create and return a new task."""
    return Task.objects.create(**params)


class TestingTaskAppViews(TestCase):
    """Test the view of task app."""
    
    def setUp(self):
        self.client = APIClient()
    
    def test_create_task(self):
        """Test creating a task."""
        