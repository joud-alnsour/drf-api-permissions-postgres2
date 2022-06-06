from django.test import TestCase
from django.urls import reverse
from rest_framework import status
# Create your tests here.

class TestDuckViews(TestCase):

    def setUp(self):
        self.client.login(username='tester', password='test')

    def test_authentication_required(self):
        self.client.logout()
        url = reverse('duck_list')
        # 403 forbidden
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)