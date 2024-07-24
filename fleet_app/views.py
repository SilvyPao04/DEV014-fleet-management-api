"""
Views for the fleet_app.
"""

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from .models import Taxi
from .serializers import TaxiSerializer

class TaxiListView(generics.ListAPIView):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['plate']