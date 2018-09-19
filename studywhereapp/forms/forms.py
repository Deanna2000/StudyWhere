from django.contrib.auth.models import User
from django import forms
from studywhereapp.models import Venue, Comment, Student


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'first_name', 'last_name')
		widgets = {
		'username': forms.TextInput(attrs={'placeholder': 'username *'}),
		'email': forms.TextInput(attrs={'placeholder': 'email *'}),
		'password': forms.TextInput(attrs={'placeholder': 'password *'}),
		'first_name': forms.TextInput(attrs={'placeholder': 'first name *'}),
		'last_name': forms.TextInput(attrs={'placeholder': 'last name *'})
		}

class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ('street', 'city', 'state', 'zip', 'phone_number')
		widgets = {
		'street': forms.TextInput(attrs={'placeholder': 'street'}),
		'city': forms.TextInput(attrs={'placeholder': 'city'}),
		'state': forms.TextInput(attrs={'placeholder': 'state'}),
		'zip': forms.TextInput(attrs={'placeholder': 'zip'}),
		'phone_number': forms.TextInput(attrs={'placeholder': 'phone number'})
		}

class VenueForm(forms.ModelForm):

	class Meta:
		model = Venue
		exclude = ["user"]
		fields = ('name', 'description', 'hours', 'price', 'food_served', 'drinks_served', 'wifi_available', 'image', 'address', 'latitude', 'longitude')
		widgets = {
			'name': forms.TextInput(attrs={'placeholder': 'name'}),
			'description': forms.TextInput(attrs={'placeholder': 'description'}),
			'hours': forms.TextInput(attrs={'placeholder': 'hours'}),
			'price': forms.TextInput(attrs={'placeholder': 'price'}),
			'address': forms.TextInput(attrs={'placeholder': 'drag the map marker to the address'}),
			'latitude': forms.TextInput(attrs={'placeholder': 'drag the map marker'}),
			'longitude': forms.TextInput(attrs={'placeholder': 'drag the map marker'})
		}

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('text',)
		widgets = { 'text': forms.TextInput(attrs={'placeholder': 'tell us about this place'})
		}



