from django.forms import forms
from django import forms
class registerForm(forms.Form):
    name = forms.CharField(label='Your name',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput())