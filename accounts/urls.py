# accounts/urls.py

from django.urls import path
from .views import index,register, login_view

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
]
