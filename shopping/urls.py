from django.urls import path
from . import views

urlpatterns = [
    path('', views.brand_list, name='home'),  # 将空路径的 URL 模式指向品牌列表视图函数
    path('brands/', views.brand_list, name='brand_list'),
    path('brands/<int:brand_id>/categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/products/', views.product_list, name='product_list'),
     path('product/chart/<str:product_id>/', views.product_price_chart, name='product_price_chart'),
]
