"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.views import ToDoUserViewSet
from todo.views import ProjectsViewSet, ToDoViewSet

router = DefaultRouter()
router.register('users', ToDoUserViewSet)
router.register('projects', ProjectsViewSet)
router.register('todos', ToDoViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='ToDo List',
        default_version='1.0',
        description='Some todo list',
        contact=openapi.Contact(email='test@mail.com'),
        license=openapi.License(name='MIT')
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', obtain_auth_token),

    path('swagger/', schema_view.with_ui()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)', schema_view.without_ui()),
]

# Добавляем в urlpatterns маршруты из роутера DRF
# urlpatterns += router.urls
