from django.shortcuts import render,get_object_or_404
from .models import Category, Brand,ProductDetail

def categories_list(request):
    categories = Category.objects.all()  # 更改变量名以反映其内容
    return render(request, 'shopping/categories_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    brands = Brand.objects.filter(category=category)
    return render(request, 'shopping/brands_list.html', {'category': category, 'brands': brands})


def brand_details(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)  # 确保 Brand 模型中有 brand_id 字段
    products = ProductDetail.objects.filter(brand=brand)  
    return render(request, 'shopping/brand_details.html', {'brand': brand, 'products': products})


