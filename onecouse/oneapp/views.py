from django.shortcuts import render
from .forms import registerForm
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
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
  
