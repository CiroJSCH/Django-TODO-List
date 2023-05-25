from django.shortcuts import render, redirect
from .models import Task
from .forms import CreateTaskForm, SignInForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "tasks.html", {"tasks": tasks})


@login_required
def task_detail(request, id):
    task = Task.objects.get(pk=id)
    return render(request, 'task_detail.html', {'task': task})


@login_required
def task_create(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            user = request.user
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


@login_required
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


@login_required
def task_delete(request, id):
    task = Task.objects.get(pk=id)
    if request.method == "POST":
        task.delete()
        return redirect("tasks")
    else:
        return render(request, "task_delete.html", {"task": task})


def signin(request):
    if request.method == "POST":
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("tasks")
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Bad data passed in. Try again.'})
    else:
        return render(request, 'login.html', {'form': SignInForm()})


def signout(request):
    logout(request)
    return redirect("login")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 != password2:
            return render(request, "signup.html", {"form": form, "error": "Passwords do not match"})
        else:
            if form.is_valid():
                user = User.objects.create_user(
                    username=request.POST["username"], password=password1)
                user.save()
                login(request, user)
                return redirect("tasks")
            else:
                return render(request, "signup.html", {"form": form, "error": "Bad data passed in. Try again."})
    else:
        form = SignUpForm()
        return render(request, "signup.html", {"form": form})
