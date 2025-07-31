from tkinter.constants import CASCADE

from django.db import models

from products.models import Product
from users.models import User


# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f'Order {self.id} by {self.user}'