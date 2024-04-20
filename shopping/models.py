from django.conf import settings
from django.db import models


# Create your models here.

class Category(models.Model):
    CategoryName = models.TextField(null=True)
    CategoryID = models.IntegerField(null=True)

    def __str__(self):
        return self.CategoryName, self.CategoryID


class Brand(models.Model):
    BrandID = models.IntegerField(primary_key=True)
    BrandName = models.TextField(null=True)  # 同样，为品牌名称提供一个字符字段
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # 设置外键关联到 Category
    
    

    def __str__(self):
        return self.BrandID,self.BrandName,self.category

class ProductDetail(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, to_field='BrandID', db_column='brand_id') # 与Brand模型关联
    ProductID=models.TextField(null=True)
    ProductName = models.CharField(max_length=255)
    BrandDesc = models.TextField(null=True)
    ProductSize=models.TextField(null=True)
    Currency=models.TextField(null=True)
    SalePrice = models.IntegerField(null=True)
    Discount=models.TextField(null=True)
    BrandID= models.IntegerField(null=True)

    def __str__(self):
        return self.ProductID,self.ProductName,self.BrandDesc,self.ProductSize,self.Currency,self.SalePrice,self.Discount,self.BrandID

