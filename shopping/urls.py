from django.urls import path,include
from . import views
from accounts.views import index
from .views import remove_from_cart,search_brand

app_name = 'shopping'
urlpatterns = [
    path('', index, name='home'),  # 将空路径的 URL 模式指向品牌列表视图函数
    path('brands/', views.brand_list, name='brand_list'),
    path('brands/<int:brand_id>/categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/products/', views.product_list, name='product_list'),
    path('product/chart/<str:product_id>/', views.product_price_chart, name='product_price_chart'),
    path('accounts/', include('accounts.urls')),
    path('search/', search_brand, name='search_brand'),
    path('search/products/', views.search_products, name='search_products'),
    path('add-to-cart/<str:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('order-details/', views.order_details, name='order_details'),
    path('view-cart/', views.view_cart, name='view_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]
