from django.shortcuts import render, redirect, HttpResponse
from .models import User, Manufacturer, Product
from .forms import RegistrationForm, LoginForm, ManufacturerCreation, ProductCreation
from django.contrib.auth import authenticate, login, logout as django_logout
from django.forms.forms import NON_FIELD_ERRORS
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
	form1 = LoginForm()
	form2 = RegistrationForm()
	if request.method == 'POST':
		# LOGIN
		if 'login' in request.POST:
			form1 = LoginForm(data=request.POST)			
			if form1.is_valid():
				user = authenticate(username=request.POST['username'], password=request.POST['password'])
				form1.full_clean()
				if user:
					login(request, user)
					request.session['id'] = user.username
					return redirect('/home')
				form1._errors[NON_FIELD_ERRORS] = form1.error_class(['User does not exist or incorrect password.'])
			# for key, value in form.errors.iteritems():
			# 	messages.error(request, value[0], extra_tags='login_error' + ' ' + key)
		# REGISTER
		if 'register' in request.POST:
			form2 = RegistrationForm(data=request.POST)
			if form2.is_valid():
				form2.save()
				return redirect('/home')
	return render(request, "accounts/index.html", {"form1":form1, "form2":form2})

# @login_required(login_url='/')
def home(request):
	if request.session['id'] == None:
		return redirect('/')
	prod = Product.objects.all()
	join = []
	for x in prod:
		join.append(Product.objects.get(id=x.combiner))
	myData = zip(prod, join)
	context = {
		'users': User.objects.all(),
		'form1': ManufacturerCreation(),
		'form2': ProductCreation(),
		'manufacturers': Manufacturer.objects.all(),
		'products': myData
	}
	return render(request, 'accounts/home.html', context)

def logout(request):
	django_logout(request)
	request.session['id'] = None
	return redirect('/')

def process(request):
	if request.method == 'POST':
		if 'man' in request.POST:
			form = ManufacturerCreation(data=request.POST)
			if form.is_valid():
				test = Manufacturer.objects.filter(name=request.POST['name'])
				if test:
					messages.error(request, 'Manufacturer already exists', extra_tags='index_error')
					return redirect('/home')
				man = Manufacturer.objects.create(name=request.POST['name'])
				man.save()
		if 'prod' in request.POST:
			form = ProductCreation(data=request.POST)
			if form.is_valid():
				man = Manufacturer.objects.filter(id=request.POST['manufacturer'])
				prod = Product.objects.create(name=request.POST['name'], combiner=request.POST['combiner'], manufacturer=man[0])
				prod.save()
	return redirect('/home')
































