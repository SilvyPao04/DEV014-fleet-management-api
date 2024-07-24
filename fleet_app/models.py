"""
Define the database structure
"""
from django.db import models

# Create your models here.
class Taxi(models.Model):
    plate = models.CharField(max_length=20)

    class Meta:
        managed = False  # Mark the model as unmanaged (Django won't create the table)
        db_table = 'taxis'  # Specify the actual database table name

    def __str__(self):
        return str(self.plate)


class Trajectory(models.Model):
    """Define the trajectories model"""
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        managed = False  # Mark the model as unmanaged (Django won't create the table)
        db_table = 'trajectories'  # Specify the actual database table name

    def __str__(self):
        return f"Trajectory for {self.taxi} at {self.date}"
