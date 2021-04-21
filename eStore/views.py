from django.shortcuts import render

from .models import *


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "eStore/index.html", context)


def cart(request):
    context = {
    }
    return render(request, "eStore/cart.html", context)
