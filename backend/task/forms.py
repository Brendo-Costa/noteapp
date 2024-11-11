"""Forms to task app."""
from django import forms
from task.models import Task



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'times', 'minutes_for_times']