from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class MainClassTest(TestCase):
    
    def test_main_view(self):
        url = reverse("main")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
    
