from django.db import models
from django.contrib.auth.models import User
from .product import Product
from .payment import Payment

# Create your models here.
class Order(models.Model):
    '''
    author: Deanna Vickers
    purpose: created instance of order
    '''
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    payment_id = models.ForeignKey('Payment', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "orders"