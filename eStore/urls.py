from django.urls import path
from . import views

urlpatterns = [
    path('items', views.item_list, name='eStore-items'),
    path('cart', views.cart, name='eStore-cart'),
]
