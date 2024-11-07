"""This file will be used to make all tests related with models."""
from django.test import TestCase
from task.models import Task



class TestingTaskAppModels(TestCase):
    """Test models."""
    
    def test_create_task(self):
        """Test creating a new task."""
        
        name = 'Study Django'
        times = 2
        time_for_times = 50
        
        task = Task.objects.create(
            name=name,
            times=times, 
            time_for_times=time_for_times,
        )
        
        initial_count = Task.objects.count()
        
        self.assertEqual(task.name, name)
        self.assertEqual(task.times, times)
        self.assertEqual(task.time_for_times, time_for_times)
        self.assertEqual(initial_count, 1)
        
    