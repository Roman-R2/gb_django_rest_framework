from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    dirthday_year = models.PositiveIntegerField()


class ToDoUser(AbstractUser):
    # Переопределил, чтобы поля нельзя было оставить пустыми
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return f'#{self.pk}-{self.username}: Name {self.first_name},' \
               f' surname {self.last_name}'
