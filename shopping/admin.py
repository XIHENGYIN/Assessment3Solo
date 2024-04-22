from django.contrib import admin
from .models import Brand, Category, Product, Order, OrderItem

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand']
    list_filter = ['brand']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'category', 'sell_price', 'original_price', 'size']
    list_filter = ['brand', 'category']
    search_fields = ['name', 'brand__name', 'category__name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at', 'total_price']
    list_filter = ['created_at', 'updated_at', 'user']
    search_fields = ['user__username']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
    list_filter = ['order', 'product']
    search_fields = ['product__name']

admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
