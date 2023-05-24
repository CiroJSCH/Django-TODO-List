from django.shortcuts import render, redirect
from .models import Task
from .forms import CreateTaskForm
from django.contrib.auth.models import User

# Create your views here.


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html", {"tasks": tasks})


def task_detail(request, id):
    task = Task.objects.get(pk=id)
    return render(request, 'task_detail.html', {'task': task})


def task_create(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            # Hardcodeado por el momento
            user = User(id=1)
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            completed = form.cleaned_data["completed"]

            task = Task(user=user, title=title, description=description,
                        completed=completed)
            task.save()
            return redirect("tasks")
        else:
            return render(request, "task_create.html", {"form": form, 'error': 'Bad data passed in. Try again.'})
    else:
        return render(request, "task_create.html", {"form": CreateTaskForm()})


def task_update(request, id):
    task = Task.objects.get(pk=id)
    if request.method == "GET":
        form = CreateTaskForm(instance=task)
        return render(request, "task_update.html", {"form": form})
    else:
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks")
        else:
            error = "Data is not valid"
            return render(request, "task_update.html", {"form": form, "error": error})
