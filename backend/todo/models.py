from django.db import models

from users.models import ToDoUser

NULLABLE = {'null': True, 'blank': True}


class ToDoModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Project(ToDoModel):
    title = models.CharField(max_length=100)
    repo_link = models.URLField(**NULLABLE)
    users = models.ManyToManyField(ToDoUser)

    def __str__(self):
        return self.title


class ToDo(ToDoModel):
    todo_text = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    todo_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    users = models.ForeignKey(ToDoUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.todo_text} (project: {self.project.title})"

    def delete(self, using=None, keep_parents=False):
        current_todo = self.is_active = False
        return current_todo

