from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html", {"tasks": tasks})
