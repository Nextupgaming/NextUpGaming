from django.shortcuts import render

def shop_home(request):
    return render(request, 'shop/home.html')


from django.shortcuts import render, get_object_or_404
from .models import Item

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'shop/item_detail.html', {'item': item})
