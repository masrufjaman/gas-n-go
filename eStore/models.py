from django.db import models
from accounts.models import *


CATEGORY_CHOICES = (
    ('P', 'Parts'),
    ('E', 'Engine'),
    ('O', 'Oil')
)


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    # image

    def __str__(self):
        return self.name


class Order(models.Model):
    username = models.ForeignKey(
        Customer, to_field='username', on_delete=models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField
    ordered = models.BooleanField(default=False)
    transaction_id = models.BooleanField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    username = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    item = models.ForeignKey(
        Item, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.item.name


class ShippingAddress(models.Model):
    username = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    area = models.CharField(max_length=200, null=True)
    road_no = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
