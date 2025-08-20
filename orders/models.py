#from django.db import models

# Create your models here.
# import uuid
# from django.conf import settings
# from django.db import models
# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f"Order {self.order_id} by {self.user.username}"



# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     def __str__(self):
#         return f"{self.product.name} (x{self.quantity})"