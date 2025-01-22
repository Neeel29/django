from task import views
from django.urls import path

urlpatterns = [
    path('task', views.task_list, name='task_list'),
]