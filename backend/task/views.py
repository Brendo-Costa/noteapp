"""Views for task app."""
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from task.serializer import TaskSerializer



class CreateTaskView(APIView):
    """
    View to create tasks and storage in database.
    """


    def post(self, request):
        """Receive a request and create a new task."""

        data = request.data
        serializer = TaskSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Task created successfully!',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'message': 'Task creation failed.',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)