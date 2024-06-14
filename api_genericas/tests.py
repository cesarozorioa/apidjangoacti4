from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
# Create your tests here.
class ReadOnlyPermissionTests(APITestCase):
    def test_read_permission(self):
        url = reverse('autores_List')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_write_permission(self):
        url = reverse('autores_List')
        data = {'name': 'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)