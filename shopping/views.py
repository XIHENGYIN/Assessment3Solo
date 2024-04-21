from django.shortcuts import render, get_object_or_404
from .models import Brand, Category, Product
import json

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'shopping/brands_list.html', {'brands': brands})

def category_list(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    categories = brand.categories.all()
    return render(request, 'shopping/categories_list.html', {'brand': brand, 'categories': categories})

def product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'shopping/products_detail.html', {'category': category, 'products': products})

def product_price_chart(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    return render(request, 'shopping/product_price_chart.html', {'product': product})

