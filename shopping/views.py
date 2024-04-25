from django.shortcuts import render, get_object_or_404,redirect
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

def search_brand(request):
    query = request.GET.get('query', '').strip()  # Get search terms and remove first and last spaces
    if query:
        # Case-insensitive lookup of brands with brand names or initials that contain search terms
        brands = Brand.objects.filter(name__icontains=query) | Brand.objects.filter(name__istartswith=query)
    else:
        brands = Brand.objects.all()  # If there are no search terms, all brands are displayed
    return render(request, 'shopping/brands_list.html', {'brands': brands})

def search_products(request):
    query = request.GET.get('query', '').strip()
    if query.isdigit():  
        products = Product.objects.filter(id=query)  # Find by ID
    else:  # Otherwise look by description
        products = Product.objects.filter(description__icontains=query)

    return render(request, 'shopping/products_detail.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    # Try to get the user's latest order
    last_order = Order.objects.filter(user=request.user).order_by('-created_at').first()
    if last_order and not last_order.items.exists():  # Check latest orders for order items
        order = last_order
    else:
        # If there are no outstanding orders, create a new order
        order = Order.objects.create(user=request.user, total_price=0)
    
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product, defaults={'price': product.sell_price})
    if not created:
        order_item.quantity += 1
        order_item.price = product.sell_price * order_item.quantity  # Update prices for individual order items
        order_item.save()
    
    order.total_price += product.sell_price  # Update order total price
    order.save()
    
    return redirect('shopping:order_details')

def order_details(request):
    # Get user's latest order
    order = Order.objects.filter(user=request.user).order_by('-created_at').first()
    if order:
        return render(request, 'shopping/order_details.html', {'order': order})
    else:
        # If there are no orders, return an empty order page or message
        return render(request, 'shopping/order_details.html', {'message': 'No active orders found.'})


def view_cart(request):
    # Try to get the user's current shopping cart
    cart = Order.objects.filter(user=request.user).order_by('-created_at').first()
    if cart and cart.items.exists():
        return render(request, 'shopping/cart_details.html', {'cart': cart})
    else:
        return render(request, 'shopping/cart_details.html', {'message': 'Your cart is empty.'})


def remove_from_cart(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id)
    item.delete()
    return redirect('shopping:view_cart')

