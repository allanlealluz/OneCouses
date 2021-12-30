from django.forms import forms
from django import forms
class registerForm(forms.Form):
    name = forms.CharField(label='Your name')
    password = forms.PasswordInput()