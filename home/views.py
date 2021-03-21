from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Home</h1>')


def about(request):
    return HttpResponse('<h1>About Us</h1>')


def help(request):
    return HttpResponse('<h1>Help</h1>')
