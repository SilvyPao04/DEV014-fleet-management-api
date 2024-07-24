from django.test import TestCase
from django.urls import reverse
from .models import Taxi

# Create your tests here.
class TaxiListViewTests(TestCase):
    
    def setUp(self):
        # Set up initial data for testing
        self.taxi1 = Taxi.objects.create(plate='ABC123')
        self.taxi2 = Taxi.objects.create(plate='XYZ789')
    
    def test_get_all_taxis(self):
        # Simulate a GET request to the taxi listing endpoint
        response = self.client.get(reverse('taxi-list'))

        # Verify the response status code
        self.assertEqual(response.status_code, 200)

        # Check if the response contains a list of taxis
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

        # Verify if each taxi object has the expected fields
        for taxi in data:
            self.assertIn('id', taxi)
            self.assertIn('plate', taxi)