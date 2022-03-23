from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from todo.models import Project, ToDo
from todo.serializers import ProjectSerializer, ToDoSerializer
from users.models import ToDoUser


class ProjectsLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectsViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    # pagination_class = ProjectsLimitOffsetPagination
    # DjangoFilterBackend - фильтрация в url /?field=значение
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title']


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    # pagination_class = ToDoLimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['todo_text', 'is_active']
