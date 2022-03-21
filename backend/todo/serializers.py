from rest_framework.serializers import ModelSerializer

from users.models import ToDoUser
from users.serializers import UserModelSerializer
from .models import Project, ToDo


class ProjectSerializer(ModelSerializer):

    # def create(self, validated_data):
    #     user = ToDoUser(**validated_data)
    #     user.save()
    #     return user

    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            'title',
            'repo_link',
            'users',
        ]


class ToDoSerializer(ModelSerializer):
    todo_project = ProjectSerializer()
    users = UserModelSerializer(many=True)

    class Meta:
        model = ToDo
        fields = [
            'todo_text',
            'is_active',
            'todo_project',
            'users',
        ]
