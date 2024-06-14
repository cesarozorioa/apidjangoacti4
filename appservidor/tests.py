from django.test import TestCase

# Create your tests here.
class Test1(TestCase):
    def test_uno(self):
        url = '/'
        request = self.client.get(url)
        self.assertEqual(request.status_code,200)
        
