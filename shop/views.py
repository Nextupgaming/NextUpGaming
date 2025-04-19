
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
