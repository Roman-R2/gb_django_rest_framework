from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .serializers import UserModelSerializer, UserModelSerializerV2
from .models import ToDoUser


class ToDoUserViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    # serializer_class = UserModelSerializer
    queryset = ToDoUser.objects.all()

    def get_serializer_class(self):
        # UserModelSerializerV2
        if self.request.version == '2.0':
            return UserModelSerializerV2
        return UserModelSerializer
