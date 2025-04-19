from django.contrib import admin
from django.urls import path, include
from shop.views import shop_home

from django.shortcuts import render

def shop_home(request):
    return render(request, 'shop/shop_home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop_home, name='shop_home'),
    path('shop/', include('shop.urls')),
    path('accounts/', include('users.urls')),
]
