from task import views
from django.urls import path

urlpatterns = [
    path('', views.task_list, name='tasks_list_or_create'),
    path('<int:pk>', views.task_action, name='task_update_or_delete'),
]