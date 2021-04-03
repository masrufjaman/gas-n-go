from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Customer
from django.contrib import messages


def register(request):

    if request.method == 'POST':
        # *Login Part
        if request.POST.get('login'):
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home-home')
            else:
                messages.error(
                    request, f'Invalid credentials...')
                return redirect('accounts-login')

        # *Registration part
        else:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            if Customer.objects.filter(username=username).exists():
                messages.error(
                    request, f'Username "{username}" already taken...')
                return redirect('accounts-register')
            elif Customer.objects.filter(email=email).exists():
                messages.error(request, f'Email "{email}" already taken...')
                return redirect('accounts-register')
            else:
                user = Customer.objects.create(
                    username=username, password=password, email=email)
                user.save()
                messages.success(request, f'Account created for {username}!')
            return redirect('home-home')

    else:
        return render(request, 'accounts/register.html', {'title': 'Register'})


def login(request):
    if request.method == 'POST':
        # *Login Part
        if request.POST.get('login'):
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home-home')
            else:
                messages.error(
                    request, f'Invalid credentials...')
                return redirect('accounts-login')

        # *Registration part
        else:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            if Customer.objects.filter(username=username).exists():
                messages.error(
                    request, f'Username "{username}" already taken...')
                return redirect('accounts-register')
            elif Customer.objects.filter(email=email).exists():
                messages.error(request, f'Email "{email}" already taken...')
                return redirect('accounts-register')
            else:
                user = Customer.objects.create(
                    username=username, password=password, email=email)
                user.save()
                messages.success(request, f'Account created for {username}!')
            return redirect('home-home')

    else:
        return render(request, 'accounts/login.html', {'title': 'Login'})


def logout(request):
    auth.logout(request)
    return redirect('home-home')
