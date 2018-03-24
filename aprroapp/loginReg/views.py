from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
<<<<<<< HEAD
		user = 	'New User!' 
		return render(request, 'loginReg/index.html' ,context= {'user':user})
=======
	return render(request, 'loginReg/index.html')
>>>>>>> 008bce6ab6032f3b05234b59349738d4d8288be8
