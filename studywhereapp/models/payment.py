from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Payment(models.Model):
    '''
    author: Deanna Vickers
    purpose: created instance of payment
    '''
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    account_number = models.CharField(max_length=50)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "payments"