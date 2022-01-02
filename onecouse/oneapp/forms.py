from django.forms import forms
from django import forms
from django.contrib.auth.forms import AuthenticationForm
class registerForm(forms.Form):
    name = forms.CharField(label='Your name',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput())
class LogForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass
