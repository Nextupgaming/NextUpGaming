
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_view, name='shop'),
    path('buy/<int:item_id>/', views.purchase_view, name='purchase_item'),
]
