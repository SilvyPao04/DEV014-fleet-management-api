"""
Serializers for the fleet_app.

This module contains the serializer classes for the fleet_app models.
The serializers convert model instances to JSON format and vice versa, 
allowing for easy interaction with the API.
"""

from rest_framework import serializers
from .models import Taxi

class TaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = '__all__'