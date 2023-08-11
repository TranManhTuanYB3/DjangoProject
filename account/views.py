from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views import View

from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm, Customer



def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=password,)
			login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)


def logout_view(request):
	logout(request)
	return redirect('/')


def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "account/login.html", context)


def account_view(request):

	if not request.user.is_authenticated:	# Xác thực xem đã đăng nhập chưa
		return redirect("login")

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST)
		if form.is_valid():
			customer = form.save(commit=False)  # Lưu mà không thực sự lưu vào database
			customer.user = request.user  # Gán giá trị cho trường user
			customer.save()
			name = form.cleaned_data.get('name')
			address = form.cleaned_data.get('address')
			phone = form.cleaned_data.get('phone')
			customer = authenticate(user=customer.user, name=name, address=address, phone=phone)
			context['success_message'] = "Updated"
		else:
			context['account_form'] = form
	else:
		form = AccountUpdateForm()
	context['account_form'] = form
	return render(request, "account/account.html", context)

def address(request):
	context = {}
	add = Customer.objects.filter(user=request.user)
	context = {
		'add': add,
	}
	return render(request, 'account/address.html', context)

def updateaddress(request, pk):
    
	if not request.user.is_authenticated:	# Xác thực xem đã đăng nhập chưa
		return redirect("login")
	
	context = {}
	add = Customer.objects.get(pk=pk)
		
	if request.POST:
		form = AccountUpdateForm(request.POST)
		if form.is_valid():
			add.name = form.cleaned_data['name']
			add.address = form.cleaned_data['address']
			add.phone = form.cleaned_data['phone']
			add.save()
			return redirect('address')
	else:
		form = AccountUpdateForm(instance=add)
		
	context['form'] = form
	return render(request, 'account/updateaddress.html', context)	