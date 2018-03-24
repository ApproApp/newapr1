from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
		user = 	'New User!' 
		return render(request, 'loginReg/index.html' ,context= {'user':user})