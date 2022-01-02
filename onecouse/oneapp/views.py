from django.contrib.auth.management import get_default_username
from django.shortcuts import render,redirect
from .forms import registerForm,LogForm
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
def index(request):
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
def login(request):
  if request.method == 'POST':
    form = LogForm(request.POST)
    nome = request.POST.get('name', False)
    password = request.POST.get('password', False)
    user = authenticate(username=nome,password=password)
    request.session['user'] = 'user'
    if user is not None:
      login(request, user)
      request.session['user'] = 'user'
      redirect('/')
  else:
    form = LogForm()
  return render(request, 'oneapp/login.html', {'form': form})