from django.db import models
from django.contrib.auth.models import User
# from django_google_maps import fields as map_fields
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Venue(models.Model):
    '''
    author: Deanna Vickers
    purpose: to build out data structure for venues that can be used for studying while at NSS.
    '''
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    # mapaddress = map_fields.AddressField(max_length=200)
    # geolocation = map_fields.GeoLocationField(max_length=100)
    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    hours = models.CharField(max_length=255, blank=True)
    comment = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=100, blank=True)
    venue_rating = models.IntegerField(
           default=1,
           validators=[MaxValueValidator(5), MinValueValidator(1)], blank=True)
    food_served = models.BooleanField(default=False)
    drinks_served = models.BooleanField(default=False)
    wifi_available = models.BooleanField(default=False)
    image = models.ImageField(upload_to='image/', default='image/none/no-image.jpg', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "venues"

