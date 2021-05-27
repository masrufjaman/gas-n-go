from django.shortcuts import render

from .models import *


def load_items(request):
    return render(request, "loads/load.html")
