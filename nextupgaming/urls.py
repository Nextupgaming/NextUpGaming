from django.contrib import admin
from django.urls import path
from shop.views import shop_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', shop_home, name='shop_home'),
]