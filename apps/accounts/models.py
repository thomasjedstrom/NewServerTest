from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import UserManager
from .mixins import CustomMixin

# VALIDATION METHODS
def validateLengthGreaterThanTwo(value):
	if len(value)< 3:
		raise ValidationError(
			'This field must be longer than 2 characters'.format(value)
		)


class User(CustomMixin, models.Model):
	username = models.CharField(max_length=100, validators = [validateLengthGreaterThanTwo], unique=True)
	first_name = models.CharField(max_length=100, validators = [validateLengthGreaterThanTwo])
	last_name = models.CharField(max_length=100, validators = [validateLengthGreaterThanTwo])
	email = models.EmailField(max_length=200, unique=True)
	password = models.CharField(max_length=255, validators = [validateLengthGreaterThanTwo])
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	last_login = models.DateTimeField(auto_now_add=True, blank=True)

	REQUIRED_FIELDS = []
	objects = UserManager()
	def __unicode__(self):
		return self.username
	class Meta:
		db_table = 'users'

	USERNAME_FIELD = 'username'

class Manufacturer(models.Model):
	name = models.CharField(max_length=100)
	class Meta:
		db_table = 'manufacturers'
	def __unicode__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=100)
	combiner = models.IntegerField()
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
	class Meta:
		db_table = 'products'
	def __unicode__(self):
		return self.name


























		