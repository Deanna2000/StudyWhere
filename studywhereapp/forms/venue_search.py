from django.contrib.auth.models import User
from django import forms
from studywhereapp.models import Venue
from django.db import models


class SearchForm(forms.ModelForm):

	"""
	Author: Deanna Vickers
	Purpose: Create form model for venue search feature
	"""

	search_bar = models.CharField(max_length = 25)

class Meta:
    model = Venue
    fields = ('name', 'address')