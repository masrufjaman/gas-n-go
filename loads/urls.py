from django.urls import path
from . import views

urlpatterns = [
    path('items', views.load_items, name='load-items'),
]
