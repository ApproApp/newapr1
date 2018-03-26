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


    def save(self, commit='True'):
        user = super(RegistrationForm, self).save(commit = False)
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.rio = self.cleaned_data.get('rio')
        user.oid = self.cleaned_data.get('oid')
        user.password1 = self.cleaned_data.get('password1')
        user.password2 = self.cleaned_data.get('password2')
        if not user.username and not user.email and not user.rio and not user.oid:
            raise forms.ValidationError('You have to write something!')
        if user.password1 != user.password2:
            raise forms.ValidationError('Two passwords are not same!')
        if commit:
            user.save()