"""
URL configuration for fleet_app.
"""

from django.urls import path
from .views import TaxiListView

urlpatterns = [
    path('taxis/', TaxiListView.as_view(), name='taxi-list'),
]
