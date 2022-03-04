from rest_framework.viewsets import ModelViewSet
from .serializers import UserModelSerializer
from .models import ToDoUser


class ToDoUserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = ToDoUser.objects.all()
