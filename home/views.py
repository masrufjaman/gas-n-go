from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html', {'title': 'About-Us'})


def help(request):
    return render(request, 'home/help.html', {'title': 'Help'})


def contact(request):
    return render(request, 'home/contact.html', {'title': 'Contact-Us'})
