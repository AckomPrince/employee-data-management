from django.shortcuts import render, redirect, reverse
from .forms import LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from employee.views import home
# Create your views here.


def authenticate(username, password):
  isAuthenticated = False
  
  try:
    user = User.objects.get(username=username)
    if check_password(password, user.password):
      isAuthenticated = True
    else:
      isAuthenticated = False
  except:
    isAuthenticated = False
    
  return isAuthenticated
      

def login(request):
  form = LoginForm()
  context = {
    'form': form
  }
  
  if request.method == 'POST':
    form = LoginForm(request.POST)
    
    if form.is_valid():
      if authenticate(form.cleaned_data.get('username'), form.cleaned_data.get('password')):
      #create a session for the user
        request.session['isLoggedIn']  = True
        request.session['username'] = form.cleaned_data.get('username')
        return HttpResponseRedirect(reverse('employee:dashboard'))
      
      else:
        context ={ **context, 'error' : 'User credentials is incorrect' }
        
  
  return render(request, 'account/login.html', context)


def logout(request):
  
  if request.session.has_key('isLoggedIn') and request.session.has_key('username'):
    del request.session['isLoggedIn']
    del request.session['username']
  
  return HttpResponseRedirect(reverse('account:auth_login'))
