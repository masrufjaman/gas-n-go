from django.db import models

class Customer (models.Model):
    Customer_Name=models.CharField(max_length=50)
    Customer_ID=models.CharField(max_length=15)
    Customer_Contact=models.CharField(max_length=14)
    Customer_License=models.CharField(max_length=50)
    Customer_Mail=models.CharField(max_length=100)

class Service_Centre (models.Model):
    Company_Name=models.CharField(max_length=50)
    ID=models.CharField(max_length=15)
    Contact_Number=models.CharField(max_length=14)
    Company_Address=models.CharField(max_length=100)
    Mail_Address=models.CharField(max_length=100)
    Service_Type=models.CharField(max_length=50)

class Employee (models.Model):
    Employee_Name=models.CharField(max_length=50)
    Employee_ID=models.CharField(max_length=15)
    Contact_Number=models.CharField(max_length=14)
    Mail_Address=models.CharField(max_length=100)

class Supplier (models.Model):
    Supplier_Name=models.CharField(max_length=50)
    Supplier_ID=models.CharField(max_length=15)
    Contact_Number=models.CharField(max_length=14)
    Mail_Address=models.CharField(max_length=100)

class Pump_Service (models.Model):
    Name=models.CharField(max_length=50)
    ID=models.CharField(max_length=15)
    Contact_Number=models.CharField(max_length=14)
    Mail_Address=models.CharField(max_length=100)
    Location=models.CharField(max_length=80)
    Service_Type=models.CharField(max_length=50)

class Vehicles (models.Model):
    Name=models.CharField(max_length=50)
    ID=models.CharField(max_length=15)
    Model=models.CharField(max_length=50)
    Registration_Number=models.CharField(max_length=20)
    Description=models.CharField(max_length=100)
    Problems=models.CharField(max_length=100)

class Parts (models.Model):
    Parts_Name=models.CharField(max_length=50)
    Parts_ID=models.CharField(max_length=20)
    Parts_Price=models.CharField(max_length=10)

class Stock (models.Model):
    Stock_Number=models.CharField(max_length=20)
    Stock_Description=models.CharField(max_length=100)
    Stock_limit=models.CharField(max_length=50)
    Stock_item=models.CharField(max_length=50)
    Stock_type=models.CharField(max_length=50)

class Booking_System (models.Model):
    Serial_Number=models.CharField(max_length=100)
    Confirmation_Code=models.CharField(max_length=50)
    Payment_type=models.CharField(max_length=50)

class Review (models.Model):
    ID=models.CharField(max_length=14)
    Rating=models.CharField(max_length=80)


