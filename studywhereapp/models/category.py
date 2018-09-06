from django.db import models

# Create your models here.
class Category(models.Model):
    '''
    author: Deanna Vickers
    purpose: separated category to be it's own model
    '''
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"