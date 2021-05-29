from django.shortcuts import render, redirect

def service(request):
    return render(request, 'services/service.html', {'title': 'Service'})
