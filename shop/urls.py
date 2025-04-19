from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_home, name='shop_home'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('orders/', views.order_history, name='order_history'),
]
