from django.contrib.auth.management import get_default_username
from django.shortcuts import render,redirect
from .forms import registerForm,LogForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, user_logged_in
from .models import Courses


def index(request):
    if request.user.is_authenticated:
        value = Courses.objects.all()
        return render(request, 'oneapp/index.html', {'value': value})
    else:
        return render(request,'oneapp/index.html')

def register(request):
  if request.method == 'POST':
    form = registerForm(request.POST)
    nome = request.POST.get('name', False)
    password = request.POST.get('password', False)
    new_user = User.objects.create_user(username=nome, password=password)
    new_user.save()
  else:
    form = registerForm()
  return render(request,'oneapp/register.html',{'form':form})
def logins(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    nome = request.POST.get('name', False)
    password = request.POST.get('password', False)
    user = authenticate(username = nome, password = password)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('/')
  else:
    form = AuthenticationForm()
  return render(request, 'oneapp/login.html', {'form': form})