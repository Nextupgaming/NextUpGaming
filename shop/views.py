
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
    if request.user.userprofile.age < 18 and item.age_restricted:
        return render(request, 'shop/restricted.html')
    # Assume user has enough coins - logic to be expanded
    Order.objects.create(user=request.user, item=item)
    return render(request, 'shop/confirmation.html', {'item': item})
