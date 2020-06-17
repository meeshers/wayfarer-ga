from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Define the home view
def home(request):
    return render(request, 'home.html')


# Auth routes
def signup(request):
    return render(request, 'signup.html')
