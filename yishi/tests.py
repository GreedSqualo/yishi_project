from django.http import response
from django.test import TestCase
from django.urls.base import reverse
from yishi.models import Products, commentP, star_rating

# Create your tests here.

def add_product(Pname, price, brand, description):
    product = Products(Pname=Pname, price=price, brand=brand,description = description)
    product.save()
    return product

def add_star_rating(star_rating1, Pname, country, n):
    rating = star_rating(star_rating=star_rating1, Pname=Pname, country=country, n=n)
    rating.save()
    return rating

def add_commentP(star_rating1, content, country, Pname):
    comment = commentP(star_rating=star_rating1, content=content, country=country, Pname=Pname)
    comment.save()
    return comment

class ProductMethodTests(TestCase):
    """
        Check wether the price of the product is bigger than 0
    """
    def test_ensure_price_are_positive(self):
        product = add_product('test', -1, 'Morrisons', 'Just a test')
        self.assertEqual((product.price > 0), True)

    """
        Check wether the slug of the product is created successfully
    """
    def test_slug_line_creation(self):
        product = add_product('test a new product', -1, 'Morrisons', 'Just a test')
        self.assertEqual(product.slug, 'test-a-new-product')

class RatingMethodTests(TestCase):
    """
        Check wether the n of star-rating is bigger than 0
    """
    def test_ensure_n_is_positive(self):
        product = add_product('test', 1, 'Morrisons', 'Just a test')
        rating = star_rating(star_rating=1, Pname=product, country='China', n=-1)
        rating.save()
        self.assertEqual((rating.n > 0), True)

    """
        Check wether the rating is positive
    """
    def test_ensure_rating_is_positive(self):
        product = add_product('test', 1, 'Morrisons', 'Just a test')
        rating = add_star_rating(-1, product, 'China', 1)
        self.assertEqual((rating.star_rating > 0), True)

class commentPMethodTest(TestCase):
    """
        Check wether the rating is bigger than 0
    """
    def test_ensure_rating_is_positive(self):
        product = add_product('test', 1, 'Morrisons', 'Just a test')
        comment = add_commentP(-1, 'Just a test', 'China', product)
        self.assertEqual((comment.star_rating > 0), True)