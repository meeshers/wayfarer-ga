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

user = User('Lolo', 'Tabby', '05-14-2020')

class Blog:
    def __init__(self,title,author,content, num):
        self.title = title
        self.author = author
        self.content = content
        self.num = num

blogs = [
    Blog('night in LA', 'Leborn James', 'play basketball game1',4),
    Blog('night in Seattle', 'Leborn James', 'play basketball game2',2),
    Blog('night in SF', 'Leborn James', 'play basketball game3',3)
]

def profile(request):
    context = {'test':user, 'blogs': blogs}
    return render(request, 'registration/profile.html',context)

def blog(request,blog_id):
    # blog = blog_id
    context = {'blogs':blogs}
    return render(request, 'blog/show.html', context)
