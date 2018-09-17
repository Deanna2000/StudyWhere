from django.contrib.auth.models import User
from django import forms
from studywhereapp.models import Venue, Comment
from studywhereapp.models import CustomerRegistration


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)

class CustomerForm(forms.ModelForm):

    class Meta:
        model = CustomerRegistration
        fields = ['street', 'city', 'state', 'zip', 'phone_number']

class VenueForm(forms.ModelForm):

    class Meta:
        model = Venue
        exclude = ["user"]
        fields = ['name', 'description', 'latitude', 'longitude', 'hours',
'address', 'price', 'venue_rating', 'food_served', 'drinks_served', 'wifi_available', 'image']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
