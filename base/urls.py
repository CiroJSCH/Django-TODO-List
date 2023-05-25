from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="tasks"),
    path("login/", views.signin, name="login"),
    path("logout/", views.signout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("task/<int:id>", views.task_detail, name="task_detail"),
    path("task/create/", views.task_create, name="task_create"),
    path("task/update/<int:id>", views.task_update, name="task_update"),
    path("task/delete/<int:id>", views.task_delete, name="task_delete"),
]
