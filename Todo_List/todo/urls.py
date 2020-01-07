from django.urls import path
from .views import list_tasks, create_task, delete_tasks

urlpatterns = [
    path('', list_tasks, name="list"),
    path('create/', create_task, name='create'),
    path('delete/<int:task_id>/', delete_tasks, name='delete')
]
