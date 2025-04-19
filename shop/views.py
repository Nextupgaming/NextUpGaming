from django.shortcuts import render
from .models import Item

def shop_home(request):
    items = Item.objects.all()
    return render(request, 'shop/shop_home.html', {'items': items})