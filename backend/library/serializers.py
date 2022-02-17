from rest_framework.serializers import ModelSerializer
from .models import Author, ToDoUser


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = ToDoUser
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
        ]
