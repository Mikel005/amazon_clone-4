from django.db import models
from products.models import Product
# from django.contrib.auth.models import User
from django.conf import settings
import uuid

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return f"{self.user.username}'s cart"
    def __str__(self):
        return f"Cart {self.order_id}"
    def total_price(self):
        return sum(item.total_price() for item in self.items.all())
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def total_price(self):
        return self.product.price * self.quantity