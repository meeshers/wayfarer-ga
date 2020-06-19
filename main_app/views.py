from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Post, City, Profile
from .forms import Edit_Form

# Create your views here.

# Define the home view
def home(request):
    return render(request, 'home.html')

# --- Auth route --- #
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

""" 
class Blog:
    def __init__(self,title,author,content, num):
        self.title = title
        self.author = author
        self.content = content
        self.num = num

blogs = [
    Blog('night in LA', 'Leborn James', 'play basketball game1',1),
    Blog('night in Seattle', 'Leborn James', 'play basketball game2',2),
    Blog('night in SF', 'Leborn James', 'play basketball game3',3)
] """

# --- User routes --- #
@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user)
    context = {'posts': posts, 'user':request.user}
    return render(request, 'registration/profile.html',context)

def blog(request,blog_id):
    #context = {'blog':blog_id,'title':blogs[blog_id].title,'author':blogs[blog_id].author,'content':blogs[blog_id].content,}
    post = Post.objects.get(id=blog_id)
    context = {'post':post}
    return render(request, 'blog/show.html', context)

@login_required
def profile_edit(request, user_id):
    if request.method == 'POST':
      profile_form = Edit_Form(request.POST, instance= request.user)
      if profile_form.is_valid():
          profile_form.save()
          return redirect('profile')
    else:
      profile_form = Edit_Form(instance=request.user)
    context = {'profile_form': profile_form}
    return render(request, 'blog/edit.html', context)