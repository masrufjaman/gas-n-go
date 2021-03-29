from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='accounts-register'),
    path('login', views.login, name='accounts-login'),
]
