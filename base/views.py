from django.shortcuts import render
from .models import Task

# Create your views here.


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html", {"tasks": tasks})


def task_detail(request, id):
    task = Task.objects.get(pk=id)
    return render(request, 'task_detail.html', {'task': task})
