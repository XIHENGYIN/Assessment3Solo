import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist

from shopping.models import Category,Brand,ProductDetail

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        Category.objects.all().delete()
        print("table dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        try:
            with open(str(base_dir) + '/shopping/ShoppingData/categories.csv', newline='') as f:
                reader = csv.reader(f, delimiter=",")
                next(reader) # skip the header line
                for row in reader:
                    print(row)

                    category = Category.objects.create(
                        CategoryName = row[0],
                        CategoryID = int(row[1]),
                    )
                    category.save()
            print("data parsed successfully")
        except FileNotFoundError:
            print("Data.csv file not found.")
            return  # suspend the process if file is not found.
        except Exception as error:
            print(f"An error occurred while parsing Data.csv: {error}")
            return  # suspend the process if any other error occurs.

        # second table
        # delete the data from the table so that if rerunning the file, no repeat values
        Brand.objects.all().delete()
        print("Brand table dropped successfully")
        # create table again
        # open the file to read it into the database
        try:
            with open(str(base_dir) + '/shopping/ShoppingData/brands.csv', newline='') as f:
                reader = csv.reader(f, delimiter=",")
                next(reader) # skip the header line
                for row in reader:
                    print(row)
                    brand = Brand.objects.create(
                        BrandName=row[0],
                        BrandID=int(row[2]),   
                    )
                    brand.save()
                    print(f"Brand created: {brand.BrandName} with BrandID {brand.BrandID}")
            print("Brand data parsed successfully")
        except FileNotFoundError:
            print("CSV file not found.")
        except Exception as error:
            print(f"An error occurred while parsing CSV file: {error}")

        # third table
        # delete the data from the table so that if rerunning the file, no repeat values
        ProductDetail.objects.all().delete()
        print("ProductDetail table dropped successfully")
        try:
            with open(str(base_dir) + '/shopping/ShoppingData/product_details.csv', newline='') as f:
                reader = csv.reader(f, delimiter=",")
                next(reader) # skip the header line
                for row in reader:
                    try:
                        brand = Brand.objects.get(id=row[8])
                        ProductDetail.objects.create(
                            ProductID=row[0],
                            ProductName=row[1],
                            BrandDesc=row[2],
                            ProductSize=row[3],
                            Currency=row[4],
                            SalePrice=int(row[6]),
                            Discount=row[7],
                            BrandID=brand.BrandID,
                            brand=brand
                        )
                        print(f"Product detail created for brand ID {brand.BrandID}")  
                    except Brand.DoesNotExist:
                        print(f"No brand found with id {row[8]}")
        except FileNotFoundError:
            print("CSV file not found.")
        except Exception as error:
            print(f"An error occurred while parsing CSV file: {error}")










                    