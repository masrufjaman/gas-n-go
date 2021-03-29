from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    return render(request, 'accounts/register.html', {'title': 'Register'})


def login(request):
    return render(request, 'accounts/login.html', {'title': 'Login'})
