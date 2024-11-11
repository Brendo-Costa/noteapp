""" Serializer for the task API view. """
from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the task object."""
    
    
    class Meta:
        model = Task
        fields = ['name', 'times', 'minutes_for_times']
    