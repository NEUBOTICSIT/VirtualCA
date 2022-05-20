from django.forms import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# class signup(forms.Form):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class meta:
#         models=candidate
#         fields =['Firstname', 'Lastname', 'email', 'mobile', 'password']


class contactform(forms.Form):
    class meta:
        models = Contact
        fields = [' Your_Name', 'Your_Email', ' Your_Subject', 'Your_Message']


widgets = {
    'Your_Name': forms.TextInput(attrs={'class': 'form-control'}),
    'Your_Email ': forms.EmailInput(attrs={'class': 'form-control'}),
    'Your_Subject': forms.TextInput(attrs={'class': 'form-control'}),
    'Your_Message': forms.TextInput(attrs={'class': 'form-control'}),
}

#
# class newsform(forms.Form):
#
#     class meta:
#         models=Heading
#         fields =['title', 'images', 'url']
#

#
# class Request_form1(forms.Form):
#
#     class meta:
#         models=Request_form
#         fields =['email', 'name', 'mobile']
#


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
