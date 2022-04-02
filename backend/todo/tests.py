from django.test import TestCase
# генерит requests для нашего api
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework import status

from todo.views import ProjectsViewSet
from users.models import ToDoUser
from users.views import ToDoUserViewSet


class TestUserApi(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        # user = User.objects.create_superuser(
        #     'denis',
        #     email='test@mail.com',
        #     password='qwerty'
        # )
        request = factory.get('/api/users')
        # force_authenticate(request, user)
        view = ProjectsViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_get_list_with_data(self):
        user = ToDoUser.objects.create_user(
            username='test',
            email='some@mail.com',
            password='123'
        )
        user.save()
        factory = APIRequestFactory()
        request = factory.get('/api/users')
        view = ToDoUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Тестирование клиента, а не только view с реквестом
    # Это не сетевой запрос
    def test_get_list_client(self):
        client = APIClient()
        response = client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
