from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html', {'title': 'About-Us'})


def contact(request):
    return render(request, 'home/contact.html', {'title': 'Conatct'})


def payment(request):
    return render(request, 'home/payment.html', {'title': 'Payment'})


def membership(request):
    return render(request, 'home/membership.html', {'title': 'Membership'})
