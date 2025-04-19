
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_in_coins = models.PositiveIntegerField()
    price_usd = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(blank=True)
    age_restricted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    shipped = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.item.name}"



from django.db import models
from django.contrib.auth.models import User
from .models import Item  # Or simply remove the line if it's redundant (since Item is already defined above)

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.quantity * self.item.price_in_coins

    def __str__(self):
        return f"{self.quantity}x {self.item.name} for {self.user.username}"
