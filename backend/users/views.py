from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .serializers import UserModelSerializer
from .models import ToDoUser


class ToDoUserViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    serializer_class = UserModelSerializer
    queryset = ToDoUser.objects.all()
