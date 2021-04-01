from django.db import models

# Create your models here.


class Customer (models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Service_Provider (models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
