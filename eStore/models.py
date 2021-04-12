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
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class Order(models.Model):
    username = models.ForeignKey(
        Customer, to_field='username', on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.username
