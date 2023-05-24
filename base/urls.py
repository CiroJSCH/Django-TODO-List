from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="tasks"),
    path("task/<int:id>", views.task_detail, name="task_detail")
]
