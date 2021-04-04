from django.db import models


class Vehicle(models.Model):

    SERVICE_CHOICES = [{'P', 'Platinum'}, {'G', 'Gold'}]
    VEHICLE_CHOICES = [{'B', 'Bike'}, {'C', 'Car'}]

    vehicle_type = models.CharField(
        choices=VEHICLE_CHOICES, max_length=1, blank=True)
    vehicle_model = models.CharField(max_length=100)
    vehicle_owner = models.CharField(max_length=100)
    vehicle_problems = models.CharField(max_length=100)
    vehicle_reg_number = models.CharField(max_length=30)
    description = models.TextField()
    service_type = models.CharField(
        choices=SERVICE_CHOICES, max_length=1, blank=True)
    submission_date = models.DateTimeField()
    year_old = models.IntegerField(null=True)
