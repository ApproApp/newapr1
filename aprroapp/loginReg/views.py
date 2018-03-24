from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("hello world <h1>Connect the page i have added in templates/loginReg/index.html then push is first. Use proper comments so that other can understand what you have coded.Make changed in model file as per frontend</h1>")