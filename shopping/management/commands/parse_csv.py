import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError



from shopping.models import Brand, Category, Product

class Command(BaseCommand):
    help = 'Load data from csv for Brands, Categories, and Products'

    def handle(self, *args, **options):
        # Dropping the data from the tables
        Product.objects.all().delete()
        Category.objects.all().delete()
        Brand.objects.all().delete()
        print("All tables dropped successfully")

        # Importing data from CSV files
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        self.load_brands(str(base_dir) + '/shopping/ShoppingData/Brands.csv')
        self.load_categories(str(base_dir) + '/shopping/ShoppingData/Categories.csv')
        self.load_products(str(base_dir) + '/shopping/ShoppingData/Product.csv')
        print("Data parsed successfully")

    def load_brands(self, filepath):
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # skip the header line
            for row in reader:
                Brand.objects.create(
                    id=int(row[1]),
                    name=row[0]
                )

    def load_categories(self, filepath):
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # skip the header line
            for row in reader:
                category = Category.objects.create(
                    name=row[0],
                    brand_id=int(row[1])
                )

    def load_products(self, filepath):
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # skip the header line
            for row in reader:
                try:
                    brand = Brand.objects.get(id=int(row[0]))
                    category_name = row[2].strip()
                    try:
                        category = Category.objects.get(name=category_name, brand=brand)
                    except Category.DoesNotExist:
                        category = Category.objects.create(name=category_name, brand=brand)
                        print(f"Created missing category: {category_name} for brand: {brand.name}")
                    
                    Product.objects.create(
                        brand=brand,
                        category=category,
                        product_id=row[3],
                        name=row[4],
                        description=row[5],
                        size=row[6],
                        currency=row[7],
                        original_price=row[8],
                        sell_price=row[9],
                        discount=row[10]
                    )  
                except Exception as e:
                    print(f"Error processing row: {row}, Error: {str(e)}")

    

   