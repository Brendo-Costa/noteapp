"""This file is responsible for the app task routes."""
from django.urls import path
from task.views import CreateTaskView


app_name = "task"

urlpatterns = [
    path("create/", CreateTaskView.as_view(), name="create"),
]
