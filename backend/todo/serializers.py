from rest_framework.serializers import ModelSerializer

from users.models import ToDoUser
from users.serializers import UserModelSerializer
from .models import Project, ToDo


class ProjectSerializer(ModelSerializer):

    # users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'repo_link',
            'users',
        ]


class ToDoSerializer(ModelSerializer):
    # todo_project = ProjectSerializer()
    # users = UserModelSerializer(many=True)

    class Meta:
        model = ToDo
        fields = [
            'todo_text',
            'is_active',
            'todo_project',
            'users',
        ]
