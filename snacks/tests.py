from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestSnack(TestCase):

    def test_status_code(self):
        url1=reverse('SnackList')
        res1=self.client.get(url1)
        self.assertEqual(res1.status_code , 200)


    def test_template_Use(self):
        url1=reverse('SnackList')
        res1=self.client.get(url1)
        self.assertTemplateUsed(res1 , 'snack_list.html')
        self.assertTemplateUsed(res1 , '_base.html')