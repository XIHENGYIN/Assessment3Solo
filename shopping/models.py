from django.conf import settings
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='categories')

class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    size = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # 允许空值
    discount = models.TextField()



