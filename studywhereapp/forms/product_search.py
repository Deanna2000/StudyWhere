from django.contrib.auth.models import User
from django import forms
from website.models import Product



class SearchForm(forms.ModelForm):

	"""
	Author: Meghan Debity
	Purpose: Create form model for product search feature
	"""

	search_bar = models.CharField(max_length = 25)

    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'quantity',)