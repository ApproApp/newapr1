from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
# Create your views here.
def index(request):
	#if the data is posted from the form
	if request.method == 'POST':
		#then form is registration from that we have created in forms.py
		form = RegistrationForm(request.POST)
		#checking out if form is valid then save it and return the response
		if form.is_valid():
			form.save()
			return HttpResponse("<h1>Thanks for registering</h1>")
		#otherwise get the username and password that is given from login form
		username = form.cleaned_data.get('username')
		raw_password = form.cleaned_data.get('password1')
		#authenticate the user
		user = authenticate(username=username, password=raw_password)
		login(request, user)
		return HttpResponse("<h1>Welcome<h1>")
	else:
		#if data is not getting posted and rather is being requested then present the registration form
		form = RegistrationForm()
		return render(request, 'loginReg/index.html', {'form': form})
