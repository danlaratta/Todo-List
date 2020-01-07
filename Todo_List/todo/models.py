from django.db import models


# Create your models here.
class TodoList(models.Model):
    date = models.DateField()
    task = models.CharField(max_length=75)

