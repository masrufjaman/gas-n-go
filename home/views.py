from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html', {'title': 'About'})


def contact(request):
    return render(request, 'home/contact.html', {'title': 'Conatct'})
