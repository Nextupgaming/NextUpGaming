from django.contrib import admin
from django.urls import path, include
from shop.views import shop_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop_home, name='shop_home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('users.urls')),
    path('shop/', include('shop.urls')),
    path('tournaments/', include('tournaments.urls')),
]
