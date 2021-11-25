from django.http import response
from django.test import TestCase
from django.urls.base import reverse
from yishi.models import Products

# Create your tests here.

def add_product(Pname, price, brand, description):
    product = Products.objects.get_or_create(Pname=Pname)
    product.price = price
    product.brand = brand
    product.description = description
    product.save()
    return product

class ProductMethodTests(TestCase):
    """
        Check wether the price of the product is bigger than 0
    """
    def test_ensure_price_are_positive(self):
        product = Products(Pname='test', price=-1, brand='Morrisons',description = 'Just a test')
        product.save()
        self.assertEqual((product.price > 0), True)

    """
        Check wether the slug of the product is created successfully
    """
    def test_slug_line_creation(self):
        product = Products(Pname='test a new product',price=1, brand='Morrisons',description = 'Just a test')
        product.save()
        self.assertEqual(product.slug, 'test-a-new-product')