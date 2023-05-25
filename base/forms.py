from django import forms
from .models import Task
from django.contrib.auth.forms import AuthenticationForm


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']


class SignInForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
