"""
Define the database structure
"""
from django.db import models

# Create your models here.
class Taxi(models.Model):
    """Define the taxi model"""
    plate = models.CharField(max_length=20)

    def __str__(self):
        return str(self.plate)


class Trajectory(models.Model):
    """Define the trajectories model"""
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"Trajectory for {self.taxi} at {self.date}"
