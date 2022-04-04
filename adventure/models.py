from django.db import models
import re


# Create your models here.


def validate_number_plate(number_plate):
    print(number_plate)
    return bool(re.search("[A-Z]{2}-[0-9]{2}-[0-9]{2}", number_plate))


class VehicleType(models.Model):
    name = models.CharField(max_length=32)
    max_capacity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=32)
    passengers = models.PositiveIntegerField()
    vehicle_type = models.ForeignKey(VehicleType, null=True, on_delete=models.SET_NULL)
    number_plate = models.CharField(max_length=10)
    matriz = [

    ]

    def __str__(self) -> str:
        return self.name

    def can_start(self) -> bool:
        return self.vehicle_type.max_capacity >= self.passengers

    def get_distribution(self):

        if self.passengers == 3:

            self.matriz = [
                [True, True],
                [True, False]
            ]

        else:
            self.matriz = [
                [True, True],
                [True, True],
                [True, False]
            ]
        return self.matriz


class Journey(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.vehicle.name} ({self.start} - {self.end})"

    def is_finished(self):
        return not(self.end is None)
