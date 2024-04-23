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
    query = request.GET.get('query', '').strip()  # 获取搜索关键词并去除首尾空格
    if query:
        # 不区分大小写地查询品牌名称或首字母包含搜索关键词的品牌
        brands = Brand.objects.filter(name__icontains=query) | Brand.objects.filter(name__istartswith=query)
    else:
        brands = Brand.objects.all()  # 如果没有搜索关键词，则显示所有品牌
    return render(request, 'shopping/brands_list.html', {'brands': brands})

def search_products(request):
    query = request.GET.get('query', '').strip()
    if query.isdigit():  # 如果查询是数字，假定它是产品 ID
        products = Product.objects.filter(id=query)  # 按 ID 查找
    else:  # 否则按描述查找
        products = Product.objects.filter(description__icontains=query)

    return render(request, 'shopping/products_detail.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    # 尝试获取用户的最新订单，这里我们暂时假设最新的订单是未完成的
    last_order = Order.objects.filter(user=request.user).order_by('-created_at').first()
    if last_order and not last_order.items.exists():  # 检查最新订单是否有订单项
        order = last_order
    else:
        # 如果没有未完成的订单，创建新订单
        order = Order.objects.create(user=request.user, total_price=0)
    
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product, defaults={'price': product.sell_price})
    if not created:
        order_item.quantity += 1
        order_item.price = product.sell_price * order_item.quantity  # 更新单个订单项的价格
        order_item.save()
    
    order.total_price += product.sell_price  # 更新订单总价
    order.save()
    
    return redirect('shopping:order_details')

def order_details(request):
    # 获取用户的最新订单
    order = Order.objects.filter(user=request.user).order_by('-created_at').first()
    if order:
        return render(request, 'shopping/order_details.html', {'order': order})
    else:
        # 如果没有订单，返回一个空订单页面或消息
        return render(request, 'shopping/order_details.html', {'message': 'No active orders found.'})


def view_cart(request):
    # 尝试获取用户的当前购物车，这里我们假设最新的订单是当前的购物车
    cart = Order.objects.filter(user=request.user).order_by('-created_at').first()
    if cart and cart.items.exists():
        return render(request, 'shopping/cart_details.html', {'cart': cart})
    else:
        return render(request, 'shopping/cart_details.html', {'message': 'Your cart is empty.'})


def remove_from_cart(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id)
    item.delete()
    return redirect('shopping:view_cart')

