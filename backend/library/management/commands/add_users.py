import json
import os

from django.conf import settings
from django.core.management import BaseCommand
from django.db import IntegrityError

from library.models import ToDoUser


class Command(BaseCommand):
    USER_DATA_FILE = os.path.join(
        settings.BASE_DIR,
        'library/management/data/simple_users.json'
    )

    def handle(self, *args, **options):
        print('------------------- начнем -----------------------')

        try:
            ToDoUser.objects.create_superuser(
                username=settings.SUPERUSER_NAME,
                email=settings.SUPERUSER_EMAIL,
                password=settings.SUPERUSER_PASSWORD,
                first_name=settings.SUPERUSER_FIRST_NAME,
                last_name=settings.SUPERUSER_LAST_NAME,
            )
            print(f'Суперпользователь {settings.SUPERUSER_NAME} добавлен!')
        except IntegrityError:
            print(f'ERROR: Суперпользователь {settings.SUPERUSER_NAME} '
                  f'уже существует!')

        with open(self.USER_DATA_FILE) as f:
            users = json.load(f)

        for user in users:
            if not ToDoUser.objects.filter(**user):
                ToDoUser.objects.create(**user)
                print(f'Пользователь {user["username"]} создан')
            else:
                print(f'ERROR: Пользователь {user["username"]} '
                      f'уже существует')

        print('---------------- скрипт закончен------------------')
