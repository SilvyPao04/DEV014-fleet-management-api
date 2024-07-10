

from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Route for the main page
    # Other routes...
]