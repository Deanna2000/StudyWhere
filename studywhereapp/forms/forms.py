from django.contrib.auth.models import User
from django import forms
from studywhereapp.models import Venue, Comment
from studywhereapp.models import StudentRegistration


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)

class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentRegistration
        fields = ['street', 'city', 'state', 'zip', 'phone_number']

class VenueForm(forms.ModelForm):

    class Meta:
        model = Venue
        exclude = ["user"]
        fields = ['name', 'description', 'hours',
 'price', 'venue_rating', 'food_served', 'drinks_served', 'wifi_available', 'image', 'address','latitude', 'longitude']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
