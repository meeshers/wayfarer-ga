from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


# Define the home view
def home(request):
    return render(request, 'home.html')


# Auth routes
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid signup please try again"
    else:
        form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class User:
  def __init__(self, name, city, register_date):
    self.name = name
    self.city = city
    self.register_date = register_date

user = [
  User('Lolo', 'Tabby', '05-14-2020')
]

def profile(request):
    context = {'user':user}
    return render(request, 'registration/profile.html',context)
# def login(request):
#     return render(request, 'registration/login.html')
