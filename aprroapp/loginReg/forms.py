from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','tabindex':1}), required="True")
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address','tabindex':1}))
    oid = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Organisation ID','tabindex':1}))
    rio = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Role in Organisation','tabindex':1}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','tabindex':2}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'tabindex': 2}))
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'oid',
            'rio',
            'password1',
            'password2',
        ]


