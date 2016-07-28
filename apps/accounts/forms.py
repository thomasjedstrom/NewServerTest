from django import forms
from .models import User, Manufacturer, Product
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
import re

def passwordRequirements(value):
	passwordREGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
	if not passwordREGEX.match(value):
		raise ValidationError(
			'Password must contain at least 8 characters, 1 uppercase, 1 lowercase, and 1 number'
		)

class RegistrationForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['password1'].validators.append(passwordRequirements)
	password1 = forms.CharField(widget=forms.PasswordInput,
								label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput,
								label="Confirm Password")
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		if commit:
			user.save()
		return user
	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
		return self.cleaned_data
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user
	class Meta:
		model = User
		exclude = 'is_admin', 'is_active', 'password', 'last_login'


class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = 'username', 'password'

class ManufacturerCreation(forms.ModelForm):
	def save(self, commit=True):
		newman = super(ManufacturerCreation, self).save(commit=False)
		if commit:
			newman.save()
		return newman
	class Meta:
		model = Manufacturer
		fields = '__all__'

class ProductCreation(forms.ModelForm):
	def save(self, commit=True):
		newprod = super(ProductCreation, self).save(commit=False)
		if commit:
			newprod.save()
		return newprod
	class Meta:
		model = Product
		fields = '__all__'














