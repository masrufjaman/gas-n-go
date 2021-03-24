from django.db import models

class Customer (models.Model):
    Customer_Name=models.CharField(max_length=100)
    Customer_ID=models.CharField(max_length=100)
    Customer_Contact=models.CharField(max_length=30)
    Customer_License=models.CharField(max_length=100)
    Customer_Mail=models.CharField(max_length=100)
