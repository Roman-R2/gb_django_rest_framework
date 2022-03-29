from django.test import TestCase
# генерит requests для нашего api
from rest_framework.test import APIRequestFactory
from rest_framework import status

from todo.views import ProjectsViewSet


class TestUserApi(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users')
        view = ProjectsViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
