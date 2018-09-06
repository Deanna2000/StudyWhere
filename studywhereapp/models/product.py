from django.contrib.auth.models import User
from django.db import models
from .category import Category
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Product(models.Model):
    '''
    author: Joe Shep
    edited: added category, date_added, rating, like, and location.
    purpose: create product object
	edited 8/23/18: changed category to be a foregin key - Deanna
    '''
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category_name = models.ForeignKey('Category', on_delete=models.CASCADE)
    date_added = models.DateField(auto_now=False, auto_now_add=False)
    rating = models.IntegerField(
           default=1,
           validators=[MaxValueValidator(5), MinValueValidator(1)])
    like = models.BooleanField(default=False)
    location = models.CharField(max_length=50)
    local_delivery = models.BooleanField(default=False)
    image = models.ImageField(upload_to='image/', default='image/none/no-image.jpg', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "products"