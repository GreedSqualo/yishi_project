import datetime
import unittest
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import response
from django.test import TestCase, Client
from django.urls.base import reverse
from django.utils import timezone
from yishi.models import Advice, Products, UserProfile, commentP, star_rating

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

class userProfileMethodTest(unittest.TestCase):
    def test_ensure_dob_is_less_than_now(self):
        user = User(username='aaa', password='123456')
        user.save()
        profile = UserProfile(user=user, dob=timezone.now() + datetime.timedelta(days=30), nationality='China')
        profile.save()
        self.assertEqual((profile.dob <= timezone.now()), True)

class indexMethodTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    """
        Check index page
    """
    def test_index(self):
        response = self.client.get(reverse('yishi:index'))
        self.assertEqual(response.status_code, 200)

class aboutMethodTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    """
        Check about page
    """
    def test_about(self):
        response = self.client.get(reverse('yishi:about'))
        self.assertEqual(response.status_code, 200)

class resultMethodTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_result(self):
        aa = add_product('aa', 1.2, 'abrand', 'just a test')
        bb = add_product('bb', 1.3, 'bbrand', 'just a test 2')
        add_star_rating(1.2, aa, 'China', 1)
        add_star_rating(1.3, bb, 'UK', 1)
        response = self.client.post(reverse('yishi:result'), {'ProductName':'aa', 'Country':'China'})
        self.assertEqual(response.status_code, 200)

class adviceMethodTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_advice(self):
        data = {
            'title' : 'title test',
            'content' : 'test test just a test',
            'state' : 'ACTIVE',
        }
        response = self.client.post(reverse('yishi:advice'), data)
        self.assertEqual(response.status_code, 200)

# class detailMethodTest(unittest.TestCase):
#     def setUp(self):
#         self.client = Client()
    
#     def test_detail(self):
#         aa = add_product('aa', 1.2, 'abrand', 'just a test')
#         response = self.client.get(reverse('yishi:detail'), {'Pname_slug':aa.slug, 'countryS':'China'})
#         self.assertEqual(response.status_code, 200)

# class postCommentPMethodTest(unittest.TestCase):
#     def setUp(self):
#         self.client = Client()

#     def test_