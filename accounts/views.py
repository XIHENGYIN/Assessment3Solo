from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test,login_required


def index(request):
    return render(request, 'accounts/index.html')
    
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 自动登录用户
            return redirect('shopping:brand_list')  # 假设你有一个名为 'home' 的路由
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('/admin/')  # 重定向超级管理员到Django admin界面
                else:
                    return redirect('shopping:brand_list')  # 普通用户重定向到主页
            else:
                messages.error(request, 'The account number or password is not correct, please try again.')
        else:
            messages.error(request, 'Form data is invalid, please check input.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})