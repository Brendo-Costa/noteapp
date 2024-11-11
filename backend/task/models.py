"""Task app models file."""
from django.db import models



class Task(models.Model):
    """
    Creates a new task instance and saves in to the database.

    Args:
        name(str): The name of the task.
        times(int): The required number of time this task will be completed.
        time_for_times(int): The number, in minutes, that each times will have.
        
    Returns:
        Task: The instance of the created Task object.
    """
    name = models.CharField(max_length=255, blank=False, null=False)
    times = models.IntegerField(blank=False, null=False)
    minutes_for_times = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return the name representation of the task."""
        return self.name
    
    def total_time(self):
        """Return the total time, in minutes, used in the task."""
        return self.times * self.minutes_for_times
