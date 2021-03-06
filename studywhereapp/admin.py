from django.contrib.gis.db import models
from django.contrib import admin
from .models import Venue, Comment
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class VenueAdmin(admin.ModelAdmin):
	formfield_overrides = {
	map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
}

admin.site.register(Venue)
admin.site.register(Comment)
