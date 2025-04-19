
from django.urls import path
from .views import shop_view, purchase_view, add_to_cart, remove_from_cart, cart_view, checkout

urlpatterns = [
    path('', shop_view, name='shop'),
    path('buy/<int:item_id>/', purchase_view, name='purchase_item'),
    path('cart/', cart_view, name='cart_view'),
    path('cart/add/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
]
