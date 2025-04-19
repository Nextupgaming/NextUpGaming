from django.shortcuts import render, redirect
from .models import Item, Order
from django.contrib.auth.decorators import login_required
from .forms import PurchaseForm

@login_required
def shop_home(request):
    items = Item.objects.all()
    return render(request, "shop/shop_home.html", {"items": items})

@login_required
def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            Order.objects.create(user=request.user, item=item, quantity=form.cleaned_data['quantity'])
            return redirect("shop_home")
    else:
        form = PurchaseForm()
    return render(request, "shop/item_detail.html", {"item": item, "form": form})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "shop/order_history.html", {"orders": orders})
