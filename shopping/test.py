from django.test import TestCase, Client
from django.urls import reverse
from .models import Brand, Category, Product, Order, OrderItem
from django.contrib.auth import get_user_model

class BrandModelTest(TestCase):
    def test_brand_creation(self):
        brand = Brand.objects.create(name="Test Brand")
        self.assertEqual(brand.name, "Test Brand")

class BrandListViewTests(TestCase):
    def setUp(self):
        Brand.objects.create(name="Test Brand")

    def test_brand_list_view(self):
        response = self.client.get(reverse('shopping:brand_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Brand")

class ProductListTests(TestCase):
    def setUp(self):
        brand = Brand.objects.create(name="Test Brand")
        category = Category.objects.create(name="Test Category", brand=brand)
        Product.objects.create(brand=brand, category=category, name="Test Product", description="Test Description", product_id="1", size="M", currency="USD", sell_price=10.00)

    def test_product_list(self):
        category_id = Category.objects.get(name="Test Category").id
        response = self.client.get(reverse('shopping:product_list', args=(category_id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")

