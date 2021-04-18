from django.shortcuts import render

from .models import *


def item_list(request):
    # context = {
    #     'items': Item.objects.all()
    # }
    return render(request, "eStore/index.html", {'title': 'E-Store'})
