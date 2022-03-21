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
    pagination_class = ProjectsLimitOffsetPagination
    # DjangoFilterBackend - фильтрация в url /?field=значение
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title']

    # def create(self, request, *args, **kwargs):
    #     print(request, *args, **kwargs)
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED,
    #                     headers=headers)

    def perform_create(self, serializer):
        serializer.validated_data['users'] = self.request.user
        serializer.save()


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    pagination_class = ToDoLimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['todo_text', 'is_active']
