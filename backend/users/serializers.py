from rest_framework.serializers import ModelSerializer
from .models import ToDoUser


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = ToDoUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]