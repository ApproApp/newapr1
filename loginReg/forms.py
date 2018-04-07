from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

#for allowing choices in role in organisation
rio_choices = [
    ('','Select your Role in Organization'),
    ('executive', 'Executive'),
    ('admin', 'Admin'),
    ('student', 'Student'),
]

#Registration form extending to usercreation form in django predefined
class RegistrationForm(UserCreationForm):
    #list of all the fields in the form with their attributes
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','tabindex':1}), required="True")
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address','tabindex':1}))
    oid = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Organisation ID','tabindex':1}))
    rio = forms.CharField(widget=forms.Select(choices=rio_choices, attrs={'class':'form-control','tabindex':1}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','tabindex':2}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'tabindex': 2}))

    class Meta:
        model = User
        #to define in which order all these fields appear
        fields = [
            'username',
            'email',
            'oid',
            'rio',
            'password1',
            'password2',
        ]

    #because we have made changes in the predefined form thus we have to define form to save the changes
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.oid = self.cleaned_data['oid']
        user.rio = self.cleaned_data['rio']

        if commit:
            user.save()

        return user



class Login(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'tabindex': 1}), required="True")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'tabindex': 2}))
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
        ]
