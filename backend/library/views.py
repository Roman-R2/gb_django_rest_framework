from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorModelSerializer, UserModelSerializer
from .models import Author, ToDoUser


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()


class ToDoUserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = ToDoUser.objects.all()
