from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
	'''
	Purpose: Additional fields for users registering on studywhere
	'''
	street = models.CharField(max_length=30, blank=True)
	city = models.CharField(max_length=30, blank=True)
	state = models.CharField(max_length=10, blank=True)
	zip = models.IntegerField(blank=True)
	phone_number = models.IntegerField(blank=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.username

	class Meta:
		db_table = "students"
