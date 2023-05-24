from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="tasks"),
    path("task/<int:id>", views.task_detail, name="task_detail"),
    path("task/create", views.task_create, name="task_create")
]
