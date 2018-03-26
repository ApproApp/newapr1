from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
# Create your views here.
def index(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponse("<h1>Thanks for registering</h1>")
	else:
		form = RegistrationForm()
		return render(request, 'loginReg/index.html', {'form': form})
