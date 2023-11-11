from rest_framework.viewsets import ModelViewSet

from ToDoLIst.models import Task
# Create your views here.
from ToDoLIst.serializers import TaskSerializer

class TaskModelViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    lookup_field = 'id'
    queryset = Task.objects.all()
