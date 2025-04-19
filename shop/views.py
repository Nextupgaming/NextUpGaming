
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Order
from django.contrib.auth.decorators import login_required

@login_required
def shop_view(request):
    items = Item.objects.all()
    return render(request, 'shop/shop.html', {'items': items})

@login_required
def purchase_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    profile = request.user.userprofile

    # Age check
    if profile.age < 18 and item.age_restricted:
        return render(request, 'shop/restricted.html')

    # Coin balance check
    if profile.coin_balance < item.price_in_coins:
        return render(request, 'shop/insufficient_coins.html', {'item': item})

    # Deduct coins and save
    profile.coin_balance -= item.price_in_coins
    profile.save()

    # Create order
    Order.objects.create(user=request.user, item=item)
    return render(request, 'shop/confirmation.html', {'item': item})



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item, CartItem, Order

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    CartItem.objects.filter(user=request.user, item=item).delete()
    return redirect('cart_view')

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum([ci.total_price() for ci in cart_items])
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    profile = request.user.userprofile
    total = sum([ci.total_price() for ci in cart_items])

    if profile.coin_balance < total:
        return render(request, 'shop/insufficient_coins.html')

    for item in cart_items:
        Order.objects.create(user=request.user, item=item.item, quantity=item.quantity)
        profile.coin_balance -= item.total_price()
    profile.save()
    cart_items.delete()
    return render(request, 'shop/checkout_complete.html')
