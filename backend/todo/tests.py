from django.test import TestCase
# генерит requests для нашего api
from rest_framework.test import APIRequestFactory, APIClient, APITestCase, \
    force_authenticate
from rest_framework import status

from todo.models import ToDo
from todo.views import ProjectsViewSet
from users.models import ToDoUser
from users.views import ToDoUserViewSet
from mixer.backend.django import mixer


class TestUserApi(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        admin = ToDoUser.objects.create_superuser(
            'admin',
            email='test@mail.com',
            password='qwerty'
        )
        request = factory.get('/api/users')
        force_authenticate(request, admin)
        view = ProjectsViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_get_list_with_data(self):
        ToDoUser.objects.create_user(
            username='test',
            email='some@mail.com',
            password='123'
        )
        factory = APIRequestFactory()
        request = factory.get('/api/users')
        view = ToDoUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(len(response.data), 1)

    # Тестирование клиента, а не только view с реквестом
    # Это не сетевой запрос
    def test_get_list_client(self):
        admin = ToDoUser.objects.create_superuser(
            'admin',
            email='test@mail.com',
            password='qwerty'
        )
        client = APIClient()
        response = client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(len(response.data), 1)


class TestUserClientApi(APITestCase):
    def setUp(self) -> None:
        self.admin = ToDoUser.objects.create_superuser(
            'admin',
            email='test@mail.com',
            password='qwerty'
        )
        self.user = ToDoUser.objects.create_user(
            username='test',
            email='some@mail.com',
            password='123'
        )
        self.author = mixer.blend(
            ToDo,
            todo_text='Do something'
        )

    def test_get_list_client_test_case(self):
        self.client.login(username='admin', password='qwerty')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # 3 потому что одного дополнительно сгенерировал mixer.blend в
        # модели "_ToDo" (в ней ссылка на модель пользователя)
        self.assertEqual(len(response.data), 3)

    def test_get_list_403(self):
        self.client.login(username='admin', password='qwerty')
        self.client.logout()
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
