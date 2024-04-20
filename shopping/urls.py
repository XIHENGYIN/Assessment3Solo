from django.urls import path
from .views import categories_list, category_detail, brand_details

urlpatterns = [
    path('', categories_list, name='categories_list'),
    path('categories/<int:category_id>/', category_detail, name='category_detail'),
    path('brands/<int:brand_id>/', brand_details, name='brand_detail'),
]
