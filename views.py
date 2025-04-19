
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Order  # Make sure Order model exists

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'shop/order_history.html', {'orders': orders})
