from asyncio.windows_events import NULL

from django.contrib.auth import login
from django.contrib.auth.models import User, Group, Permission
from django.test import TestCase
from django.urls import reverse

from app_shops.models import Products

NUMBER_OF_PRODUCTS = 10
class ProductsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for item_index in range(NUMBER_OF_PRODUCTS):
            Products.objects.create(
                title='1',
                price='1',
                price_with_store='0.5',
                quantity='120',
            )

#
    def test_records_exists_at_desired_lacation(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marketplace/products_list.html')


    def test_records_number(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['products_list']) == NUMBER_OF_PRODUCTS)





