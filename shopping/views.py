from django.shortcuts import render, get_object_or_404
from .models import Brand, Category, Product,Order, OrderItem
from django.contrib.auth.decorators import login_required
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

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, is_open=True)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product, defaults={'price': product.sell_price})
    order_item.quantity += 1
    order_item.save()
    return redirect('shopping:order_details')

def order_details(request):
    order = get_object_or_404(Order, user=request.user, is_open=True)
    return render(request, 'shopping/order_details.html', {'order': order})

